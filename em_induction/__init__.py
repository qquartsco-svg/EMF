"""Electromagnetic Induction Foundation — Feynman Vol.2 Ch.16–17 style layers."""

from .contracts import (
    EMInductionReport,
    FaradayEMFInput,
    FaradayEMFResult,
    FluxRulePedagogyInput,
    FluxRulePedagogyResult,
    LumpedInductorInput,
    LumpedInductorResult,
    MagneticFluxInput,
    MagneticFluxResult,
    ReadinessVerdict,
    StaticRegimeInput,
    StaticRegimeResult,
)
from .ecosystem_bridges import collect_ecosystem_hints, try_em_boundary_bridge
from .faraday_emf import screen_faraday_emf
from .flux_rule_pedagogy import screen_flux_rule_pedagogy
from .foundation import analyze
from .lumped_inductor import screen_lumped_inductor
from .magnetic_flux import screen_magnetic_flux
from .static_regime import screen_static_regime

__all__ = [
    "EMInductionReport",
    "FaradayEMFInput",
    "FaradayEMFResult",
    "FluxRulePedagogyInput",
    "FluxRulePedagogyResult",
    "LumpedInductorInput",
    "LumpedInductorResult",
    "MagneticFluxInput",
    "MagneticFluxResult",
    "ReadinessVerdict",
    "StaticRegimeInput",
    "StaticRegimeResult",
    "analyze",
    "collect_ecosystem_hints",
    "screen_faraday_emf",
    "screen_flux_rule_pedagogy",
    "screen_lumped_inductor",
    "screen_magnetic_flux",
    "screen_static_regime",
    "try_em_boundary_bridge",
]
