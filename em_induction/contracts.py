"""Electromagnetic Induction Foundation — contracts (Feynman Vol.2 Ch.16–17 style screening)."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class ReadinessVerdict(Enum):
    OPERATIONAL = "operational"
    FEASIBLE = "feasible"
    EXPERIMENTAL = "experimental"
    NOT_FEASIBLE = "not_feasible"


# ── L1: electrostatic / stationary-field approximation ─────────────

@dataclass(frozen=True)
class StaticRegimeInput:
    """When any are true, pure electrostatic (∮E·dl=0) story is weaker."""
    time_varying_magnetic_field: bool = False
    conductor_loop_or_flux_area_changes: bool = False
    chemical_or_thermal_emf_in_loop: bool = False
    significant_displacement_current: bool = False


@dataclass(frozen=True)
class StaticRegimeResult:
    """1 ≈ can lean on conservative E-field / scalar potential language."""
    electrostatic_story_validity_0_1: float
    induction_relevance_0_1: float
    omega: float
    notes: str = ""


# ── L2: uniform-B flux toy (scalar Φ through flat loop) ──────────────

@dataclass(frozen=True)
class MagneticFluxInput:
    b_field_t: float = 0.1
    loop_area_m2: float = 1e-4
    """Angle between B and loop normal (rad); 0 = parallel to normal."""
    theta_rad: float = 0.0
    n_turns: int = 1


@dataclass(frozen=True)
class MagneticFluxResult:
    flux_weber: float
    omega: float
    notes: str = ""


# ── L3: Faraday law (SI) ℰ = − N dΦ/dt ───────────────────────────────

@dataclass(frozen=True)
class FaradayEMFInput:
    n_turns: int = 1
    """Direct flux derivative (Wb/s)."""
    dflux_dt_weber_per_s: Optional[float] = None
    """Or finite difference: (Φ₁−Φ₀)/Δt."""
    flux_t0_weber: Optional[float] = None
    flux_t1_weber: Optional[float] = None
    delta_t_s: Optional[float] = None


@dataclass(frozen=True)
class FaradayEMFResult:
    emf_volts: float
    lenz_summary: str
    omega: float
    notes: str = ""


# ── L4: flux-rule pedagogy (Feynman §17–2 style caveats) ─────────────

@dataclass(frozen=True)
class FluxRulePedagogyInput:
    sliding_rod_or_contracting_loop: bool = False
    moving_contact_or_switching_topology: bool = False
    betatron_or_image_charge_subtlety: bool = False
    """User thinks flux rule vs Lorentz force might disagree."""
    user_notes_ambiguity: bool = False


@dataclass(frozen=True)
class FluxRulePedagogyResult:
    """Higher → pay attention to how flux is defined through the loop."""
    flux_rule_subtlety_0_1: float
    omega: float
    notes: str = ""


# ── L5: lumped inductor proxy V = −L dI/dt ───────────────────────────

@dataclass(frozen=True)
class LumpedInductorInput:
    inductance_h: float = 1e-3
    di_dt_a_per_s: float = 0.0


@dataclass(frozen=True)
class LumpedInductorResult:
    emf_volts: float
    omega: float
    notes: str = ""


# ── Report ──────────────────────────────────────────────────────────

@dataclass
class EMInductionReport:
    static_regime: Optional[StaticRegimeResult] = None
    magnetic_flux: Optional[MagneticFluxResult] = None
    faraday_emf: Optional[FaradayEMFResult] = None
    flux_rule_pedagogy: Optional[FluxRulePedagogyResult] = None
    lumped_inductor: Optional[LumpedInductorResult] = None
    omega_em: float = 0.0
    verdict: ReadinessVerdict = ReadinessVerdict.EXPERIMENTAL
    key_bottleneck: str = ""
    disclaimer: str = ""
    feynman_chapter_hints: tuple[str, ...] = field(default_factory=tuple)
    ecosystem_hints: dict = field(default_factory=dict)
