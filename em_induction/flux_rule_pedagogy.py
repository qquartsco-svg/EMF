"""L4 — When the naive flux rule needs care (Feynman Vol.2 §17–2 narrative)."""

from __future__ import annotations

from .contracts import FluxRulePedagogyInput, FluxRulePedagogyResult


def screen_flux_rule_pedagogy(inp: FluxRulePedagogyInput) -> FluxRulePedagogyResult:
    score = 0.0
    parts = []
    if inp.sliding_rod_or_contracting_loop:
        score += 0.35
        parts.append("sliding rod / changing boundary: define flux through moving loop carefully")
    if inp.moving_contact_or_switching_topology:
        score += 0.3
        parts.append("moving contacts / topology change: flux rule vs line-integral viewpoints")
    if inp.betatron_or_image_charge_subtlety:
        score += 0.2
        parts.append("accelerator / symmetric setups: subtleties like betatron condition (textbook)")
    if inp.user_notes_ambiguity:
        score += 0.15
        parts.append("user-flagged ambiguity: re-specify the surface bounded by the loop")
    if not parts:
        parts.append("no extra caveats flagged: elementary flux-rule use may suffice for pedagogy")
        score = 0.25
    subtlety = min(1.0, score)
    omega = max(0.0, min(1.0, 0.5 + 0.4 * subtlety))
    return FluxRulePedagogyResult(
        flux_rule_subtlety_0_1=round(subtlety, 4),
        omega=round(omega, 4),
        notes="; ".join(parts),
    )
