from __future__ import annotations

from em_induction import (
    FaradayEMFInput,
    MagneticFluxInput,
    StaticRegimeInput,
    analyze,
    screen_faraday_emf,
    screen_magnetic_flux,
    screen_static_regime,
)


def test_analyze_demo_stack():
    rep = analyze()
    assert rep.static_regime is not None
    assert rep.magnetic_flux is not None
    assert rep.faraday_emf is not None
    assert rep.flux_rule_pedagogy is not None
    assert rep.lumped_inductor is not None
    assert rep.omega_em > 0
    assert len(rep.feynman_chapter_hints) == 2


def test_flux_uniform_b():
    r = screen_magnetic_flux(MagneticFluxInput(b_field_t=1.0, loop_area_m2=1.0, theta_rad=0.0, n_turns=1))
    assert abs(r.flux_weber - 1.0) < 1e-9


def test_faraday_sign_finite_difference():
    # Φ decreases → dΦ/dt < 0 → ℰ = −N dΦ/dt > 0 for N>0
    r = screen_faraday_emf(
        FaradayEMFInput(
            n_turns=2,
            flux_t0_weber=0.002,
            flux_t1_weber=0.001,
            delta_t_s=0.01,
        )
    )
    assert r.emf_volts > 0


def test_static_regime_more_flags_lower_validity():
    quiet = screen_static_regime(StaticRegimeInput())
    busy = screen_static_regime(
        StaticRegimeInput(
            time_varying_magnetic_field=True,
            conductor_loop_or_flux_area_changes=True,
            chemical_or_thermal_emf_in_loop=True,
        )
    )
    assert busy.electrostatic_story_validity_0_1 < quiet.electrostatic_story_validity_0_1


def test_partial_analyze_only_faraday():
    rep = analyze(
        faraday_emf_input=FaradayEMFInput(
            n_turns=1,
            dflux_dt_weber_per_s=0.05,
        ),
        lumped_inductor_input=None,
    )
    assert rep.faraday_emf is not None
    assert rep.static_regime is None
    assert rep.magnetic_flux is None
    assert rep.lumped_inductor is None
    assert abs(rep.faraday_emf.emf_volts - (-0.05)) < 1e-9
