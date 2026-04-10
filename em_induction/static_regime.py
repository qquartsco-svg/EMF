"""L1 — When is electrostatic / scalar-potential language enough?"""

from __future__ import annotations

from .contracts import StaticRegimeInput, StaticRegimeResult


def screen_static_regime(inp: StaticRegimeInput) -> StaticRegimeResult:
    flags = [
        inp.time_varying_magnetic_field,
        inp.conductor_loop_or_flux_area_changes,
        inp.chemical_or_thermal_emf_in_loop,
        inp.significant_displacement_current,
    ]
    n = sum(1 for f in flags if f)
    # More induction-like flags → lower pure-electrostatic story validity
    validity = max(0.0, 1.0 - 0.22 * n)
    induction_rel = min(1.0, 0.15 + 0.22 * n)
    omega = max(0.0, min(1.0, 0.42 + 0.28 * validity + 0.25 * min(induction_rel, 1.0)))
    parts = []
    if inp.time_varying_magnetic_field:
        parts.append("∂B/∂t ≠ 0 suggests Faraday / non-conservative E contribution")
    if inp.conductor_loop_or_flux_area_changes:
        parts.append("changing flux area or motion: check motional EMF vs flux rule")
    if inp.chemical_or_thermal_emf_in_loop:
        parts.append("non-Coulomb source in loop (battery-like): total EMF ≠ −∫E_conservative·dl")
    if inp.significant_displacement_current:
        parts.append("displacement current may matter for Ampère–Maxwell context")
    if not parts:
        parts.append("no strong induction flags: scalar potential / electrostatics often a fair first pass")
    return StaticRegimeResult(
        electrostatic_story_validity_0_1=round(validity, 4),
        induction_relevance_0_1=round(induction_rel, 4),
        omega=round(omega, 4),
        notes="; ".join(parts),
    )
