from __future__ import annotations

import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from em_induction import analyze, FaradayEMFInput


def main() -> None:
    rep = analyze()
    print("demo omega_em =", rep.omega_em, "verdict =", rep.verdict.value)
    print("Faraday EMF (V) =", rep.faraday_emf.emf_volts if rep.faraday_emf else None)
    print("hints:", rep.feynman_chapter_hints)

    rep2 = analyze(
        faraday_emf_input=FaradayEMFInput(n_turns=100, dflux_dt_weber_per_s=1e-4),
        static_regime_input=None,
        magnetic_flux_input=None,
        lumped_inductor_input=None,
    )
    print("100 turns, dΦ/dt=1e-4 Wb/s → EMF (V) =", rep2.faraday_emf.emf_volts if rep2.faraday_emf else None)


if __name__ == "__main__":
    main()
