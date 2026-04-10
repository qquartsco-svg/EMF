"""L5 — Lumped inductor EMF proxy V = −L dI/dt."""

from __future__ import annotations

from .contracts import LumpedInductorInput, LumpedInductorResult


def screen_lumped_inductor(inp: LumpedInductorInput) -> LumpedInductorResult:
    L = max(inp.inductance_h, 1e-18)
    emf = -L * inp.di_dt_a_per_s
    omega = 0.55
    if abs(inp.di_dt_a_per_s) > 0:
        omega += 0.25
    if 1e-12 <= L <= 1e3:
        omega += 0.1
    omega = min(1.0, omega)
    return LumpedInductorResult(
        emf_volts=round(emf, 10),
        omega=round(omega, 4),
        notes="Lumped-element toy; ignores radiation, skin effect, and coupled coils unless extended.",
    )
