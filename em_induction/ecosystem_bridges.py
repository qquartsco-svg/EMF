"""Bridges to earlier Vol.2-aligned foundations on _staging."""

from __future__ import annotations

import os
import sys
from typing import Any

_STAGING = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _path(name: str) -> bool:
    p = os.path.join(_STAGING, name)
    if not os.path.isdir(p):
        return False
    if p not in sys.path:
        sys.path.insert(0, p)
    return True


def try_em_boundary_bridge() -> dict[str, Any]:
    """Electrostatics / boundary / flux-circulation screening (Feynman Vol.2 early chapters)."""
    if not _path("01_A_Electromagnetic_Boundary_Foundation"):
        return {"status": "unavailable", "reason": "01_A_Electromagnetic_Boundary_Foundation not on path"}
    try:
        from em_boundary.contracts import EPSILON_0, MU_0

        return {
            "status": "available",
            "bridge": "01_A_Electromagnetic_Boundary_Foundation",
            "epsilon_0": EPSILON_0,
            "mu_0": MU_0,
            "notes": "Upstream layer for ∇×E=0 electrostatics before induction dominates.",
        }
    except Exception as e:
        return {"status": "error", "detail": str(e)}


def try_atmospheric_electric_bridge() -> dict[str, Any]:
    """Feynman Vol.2 Ch.9–10 global circuit & dielectric narrative."""
    if not _path("Atmospheric_Electric_Circuit_Foundation"):
        return {"status": "unavailable", "reason": "Atmospheric_Electric_Circuit_Foundation not on path"}
    try:
        return {
            "status": "available",
            "bridge": "Atmospheric_Electric_Circuit_Foundation",
            "notes": "Ch.9–10: spherical capacitor model, return current, polarization — before Ch.17 formalism.",
        }
    except Exception as e:
        return {"status": "error", "detail": str(e)}


def try_optics_bridge_via_em(*, wavelength_m: float = 550e-9) -> dict[str, Any]:
    if not _path("01_A_Electromagnetic_Boundary_Foundation"):
        return {"status": "unavailable", "reason": "EM boundary not on path"}
    try:
        from em_boundary.ecosystem_bridges import try_optics_bridge

        pl = try_optics_bridge(wavelength_m=wavelength_m)
        if pl is None:
            return {"status": "unavailable", "reason": "Optics bridge returned None"}
        return {"status": "available", "bridge": "Optics via em_boundary", "payload": pl}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


def collect_ecosystem_hints(*, wavelength_m: float = 550e-9) -> dict[str, Any]:
    return {
        "em_boundary": try_em_boundary_bridge(),
        "atmospheric_electric": try_atmospheric_electric_bridge(),
        "optics": try_optics_bridge_via_em(wavelength_m=wavelength_m),
    }
