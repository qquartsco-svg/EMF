"""L2 — Uniform B through flat N-turn loop (scalar flux toy)."""

from __future__ import annotations

import math

from .contracts import MagneticFluxInput, MagneticFluxResult


def screen_magnetic_flux(inp: MagneticFluxInput) -> MagneticFluxResult:
    b = inp.b_field_t
    a = max(inp.loop_area_m2, 1e-30)
    n = max(1, int(inp.n_turns))
    phi = n * b * a * math.cos(inp.theta_rad)
    # omega: reasonable parameter ranges for pedagogy
    omega = 0.5
    if 1e-6 <= a <= 10.0 and abs(b) < 100.0:
        omega += 0.25
    if n <= 10_000:
        omega += 0.15
    omega = min(1.0, omega)
    notes = f"Φ = N B A cosθ = {phi:.6g} Wb (uniform-B flat-loop toy)"
    return MagneticFluxResult(flux_weber=round(phi, 12), omega=round(omega, 4), notes=notes)
