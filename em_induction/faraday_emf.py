"""L3 — Faraday: ℰ = − N dΦ/dt (SI)."""

from __future__ import annotations

from .contracts import FaradayEMFInput, FaradayEMFResult


def screen_faraday_emf(inp: FaradayEMFInput) -> FaradayEMFResult:
    n = max(1, int(inp.n_turns))
    dphi_dt = inp.dflux_dt_weber_per_s
    if dphi_dt is None:
        if (
            inp.flux_t0_weber is None
            or inp.flux_t1_weber is None
            or inp.delta_t_s is None
            or inp.delta_t_s <= 0
        ):
            return FaradayEMFResult(
                emf_volts=0.0,
                lenz_summary="insufficient input for dΦ/dt",
                omega=0.2,
                notes="Provide dflux_dt_weber_per_s or (flux_t0, flux_t1, delta_t_s).",
            )
        dphi_dt = (inp.flux_t1_weber - inp.flux_t0_weber) / inp.delta_t_s
    emf = -n * dphi_dt
    lenz = (
        "Φ increasing → EMF tends to drive current whose B opposes the increase (Lenz heuristic)."
        if dphi_dt > 0
        else "Φ decreasing → EMF tends to oppose that decrease (Lenz heuristic)."
        if dphi_dt < 0
        else "dΦ/dt ≈ 0 → little induced EMF from Faraday term."
    )
    omega = 0.55
    if dphi_dt != 0:
        omega += 0.25
    if abs(emf) < 1e6:
        omega += 0.1
    omega = min(1.0, omega)
    notes = "Screening only — not a full circuit model with resistance, capacitance, or radiation."
    return FaradayEMFResult(
        emf_volts=round(emf, 10),
        lenz_summary=lenz,
        omega=round(omega, 4),
        notes=notes,
    )
