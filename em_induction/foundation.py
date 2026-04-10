"""Integrator — L1–L5 electromagnetic induction screening (Feynman Vol.2 narrative)."""

from __future__ import annotations

from typing import Optional

from .contracts import (
    EMInductionReport,
    FaradayEMFInput,
    FluxRulePedagogyInput,
    LumpedInductorInput,
    MagneticFluxInput,
    ReadinessVerdict,
    StaticRegimeInput,
)
from .ecosystem_bridges import collect_ecosystem_hints
from .faraday_emf import screen_faraday_emf
from .flux_rule_pedagogy import screen_flux_rule_pedagogy
from .lumped_inductor import screen_lumped_inductor
from .magnetic_flux import screen_magnetic_flux
from .static_regime import screen_static_regime


def _verdict(omega: float) -> ReadinessVerdict:
    if omega >= 0.78:
        return ReadinessVerdict.OPERATIONAL
    if omega >= 0.52:
        return ReadinessVerdict.FEASIBLE
    if omega >= 0.28:
        return ReadinessVerdict.EXPERIMENTAL
    return ReadinessVerdict.NOT_FEASIBLE


def analyze(
    *,
    static_regime_input: Optional[StaticRegimeInput] = None,
    magnetic_flux_input: Optional[MagneticFluxInput] = None,
    faraday_emf_input: Optional[FaradayEMFInput] = None,
    flux_rule_pedagogy_input: Optional[FluxRulePedagogyInput] = None,
    lumped_inductor_input: Optional[LumpedInductorInput] = None,
    attach_ecosystem_hints: bool = False,
) -> EMInductionReport:
    """If all three core inputs are None, runs a small demo stack (teaching numbers).

    If you pass any of static_regime_input / magnetic_flux_input / faraday_emf_input, only those
    non-None layers run (plus flux_rule_pedagogy always; lumped_inductor if provided).
    """
    demo = (
        static_regime_input is None
        and magnetic_flux_input is None
        and faraday_emf_input is None
    )
    if demo:
        static_regime_input = StaticRegimeInput(time_varying_magnetic_field=True)
        magnetic_flux_input = MagneticFluxInput(
            b_field_t=0.2, loop_area_m2=0.01, theta_rad=0.0, n_turns=2
        )
        faraday_emf_input = FaradayEMFInput(
            n_turns=2,
            flux_t0_weber=0.002,
            flux_t1_weber=0.001,
            delta_t_s=0.01,
        )
        if lumped_inductor_input is None:
            lumped_inductor_input = LumpedInductorInput(inductance_h=5e-4, di_dt_a_per_s=100.0)

    if flux_rule_pedagogy_input is None:
        flux_rule_pedagogy_input = FluxRulePedagogyInput()

    sr = screen_static_regime(static_regime_input) if static_regime_input else None
    mf = screen_magnetic_flux(magnetic_flux_input) if magnetic_flux_input else None
    fe = screen_faraday_emf(faraday_emf_input) if faraday_emf_input else None
    fr = screen_flux_rule_pedagogy(flux_rule_pedagogy_input)
    li = screen_lumped_inductor(lumped_inductor_input) if lumped_inductor_input else None

    omegas: list[float] = []
    layers: list[tuple[str, float]] = []
    if sr:
        omegas.append(sr.omega)
        layers.append(("static_regime", sr.omega))
    if mf:
        omegas.append(mf.omega)
        layers.append(("magnetic_flux", mf.omega))
    if fe:
        omegas.append(fe.omega)
        layers.append(("faraday_emf", fe.omega))
    omegas.append(fr.omega)
    layers.append(("flux_rule_pedagogy", fr.omega))
    if li:
        omegas.append(li.omega)
        layers.append(("lumped_inductor", li.omega))

    omega_em = sum(omegas) / max(len(omegas), 1)
    bottleneck = min(layers, key=lambda x: x[1])[0] if layers else ""

    disclaimer = (
        "Electromagnetic Induction Foundation is pedagogy and order-of-magnitude screening — "
        "not Maxwell FDTD, not SPICE, not a substitute for Feynman or Jackson."
    )
    hints: dict = {}
    if attach_ecosystem_hints:
        hints = collect_ecosystem_hints()

    return EMInductionReport(
        static_regime=sr,
        magnetic_flux=mf,
        faraday_emf=fe,
        flux_rule_pedagogy=fr,
        lumped_inductor=li,
        omega_em=round(omega_em, 4),
        verdict=_verdict(omega_em),
        key_bottleneck=bottleneck,
        disclaimer=disclaimer,
        feynman_chapter_hints=(
            "Feynman Lectures Vol. II — Ch.16 Induced currents (motivation)",
            "Feynman Lectures Vol. II — Ch.17 Laws of induction (EMF, flux rule, caveats)",
        ),
        ecosystem_hints=hints,
    )
