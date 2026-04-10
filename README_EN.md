> **English.** Korean (정본): [README.md](README.md)

# EMF — Electromagnetic Induction Foundation `v0.1.0`

| Item | Value |
|------|-------|
| Version | `v0.1.0` |
| Tests | Current baseline: **5 passed** (`pytest`) |
| Python | `>=3.10` |
| Dependencies | Runtime: mostly stdlib · dev: `pytest>=8.0` |
| License | MIT |

**Electromotive force (EMF) and magnetic induction** as **L1–L5 screening layers** aligned with Feynman *Lectures on Physics* **Vol. II, roughly Ch.16–17**. The public repo name **EMF** is a short label for that theme.

**Core:** the textbook Faraday form **ℰ = − N dΦ/dt** (SI) and the circuit idiom **V = −L dI/dt** as **pedagogical proxies**. This is **not** a replacement for **FDTD, SPICE, or full Maxwell solvers**.

**Korean canonical:** [README.md](README.md) · Curriculum map: [docs/FEYNMAN_VOL2_LAYER_MAP_EN.md](docs/FEYNMAN_VOL2_LAYER_MAP_EN.md)

---

## Contents

| Section | Topic |
|---------|--------|
| [Concept](#1-concept-emf-and-layers) | EMF, flux, Faraday, flux-rule caveats |
| [Layers](#2-layers-l1l5) | L1–L5 with one-line expansion |
| [`omega_em` · `verdict`](#3-omega_em-and-verdict) | Aggregate Ω and verdict bands |
| [Extensibility](#4-extensibility-and-use) | Bridges, place in 00_BRAIN |
| [Security](#5-security-and-integrity) | SHA-256 manifest, limits |
| [Roadmap](#6-roadmap) | Possible extensions vs out-of-scope |
| [Quick start](#7-quick-start) | Install, tests, examples |

---

## 1. Concept (EMF and layers)

- **EMF:** in the Feynman Ch.17 narrative, the line integral of tangential force per unit charge around a conducting loop. Pure **electrostatics** usually gives a **conservative** **E** and **zero** circulation; **changing flux**, **motion**, **chemical sources**, etc. motivate **non-conservative** pieces and **induced EMF**.
- **Flux Φ:** L2 uses a **uniform B, flat loop** toy: **Φ = NBAcosθ**.
- **Faraday:** L3 implements **ℰ = −N dΦ/dt**.
- **Flux-rule pedagogy:** L4 flags setups where **defining the surface bounded by the loop** needs care (Feynman §17–2 style).

Longer concept: [CONCEPT_EN.md](CONCEPT_EN.md)

---

## 2. Layers (L1–L5)

| Layer | One-liner | A bit more |
|-------|-----------|------------|
| **L1** | When the electrostatic story breaks | Flags ∂B/∂t, loop motion/deformation, chemical EMF, displacement current → **conservative-E-only** vs **induction relevance** proxies |
| **L2** | Flux definition and geometry | Uniform **B**, flat loop, **N** turns, **θ** → **Φ** (non-uniform fields / 3D geometry out of scope) |
| **L3** | Faraday-induced EMF | **ℰ = −N dΦ/dt** or finite-difference **ΔΦ/Δt** |
| **L4** | Flux-rule caution cases | Sliding rod, moving contacts, betatron-style flags → **pedagogical subtlety** score |
| **L5** | Lumped inductor circuit proxy | **V = −L dI/dt** — one slice of circuit language |

---

## 3. `omega_em` and `verdict`

**`omega_em`** is approximately the **mean Ω** over layers that ran. **`verdict`** maps it to a **screening label** (not a lab or design sign-off).

| `omega_em` range | `verdict` |
|------------------|-----------|
| **≥ 0.78** | `operational` |
| **≥ 0.52** | `feasible` |
| **≥ 0.28** | `experimental` |
| **< 0.28** | `not_feasible` |

---

## 4. Extensibility and use

- **`ecosystem_bridges`:** when sibling `_staging` folders exist, shallow hooks to **`01_A`**, **`Atmospheric_Electric_Circuit`**, and **Optics** (via EM boundary).
- **Upstream:** electrostatics belongs primarily in **`Electromagnetic_Boundary_Foundation`** (its README points here for Ch.16–17).
- **Related narrative (no dedicated bridge required):** **nano-scale** induction sensitivity can be read alongside **`Nano_Scale_Foundation`** as a conceptual neighbor.
- **Downstream:** multi-phase media, transformer detail, **mutual inductance matrices**, FDTD — expect **separate** engines/tools.
- **Pedagogy:** `omega_em` / `verdict` are **observer-style** checks, not final physics verdicts.

---

## 5. Security and integrity

- **`SIGNATURE.sha256`:** a **SHA-256 file manifest** for the release tree — **not** a cryptocurrency ledger.
- **Use:** quick check that a clone matches the **intended file set**.
- **Limits:** does **not** certify physical truth, lab reproducibility, or **runtime safety**. Prefer **signed commits, CI, and provenance** for supply-chain assurance.

```bash
python3 scripts/generate_signature.py
python3 scripts/verify_signature.py
python3 scripts/verify_package_identity.py
python3 scripts/release_check.py
```

Details: [BLOCKCHAIN_INFO.md](BLOCKCHAIN_INFO.md) · [BLOCKCHAIN_INFO_EN.md](BLOCKCHAIN_INFO_EN.md)

---

## 6. Roadmap

**In-repo extensions that may fit:**

- Motional EMF (**v×B**) side-by-side with flux rule, same inputs
- **Two-coil** mutual-inductance toy
- More sibling bridges (e.g. frequency / MR foundations)

**Out of scope (separate projects):**

- Maxwell **FDTD/FEM**, **SPICE-class** simulation
- Hysteresis, radiation, full magnetostatics solvers

---

## 7. Quick start

```bash
git clone https://github.com/qquartsco-svg/EMF.git
cd EMF
pip install -e ".[dev]"
pytest tests/
python3 examples/run_em_induction_demo.py
```

### Example — full demo stack

```python
from em_induction import analyze

rep = analyze()
print(rep.omega_em, rep.verdict.value, rep.faraday_emf.emf_volts)
print(rep.disclaimer)
```

### Example — changing flux only (Faraday / L3 focus)

```python
from em_induction import analyze, FaradayEMFInput, MagneticFluxInput, StaticRegimeInput

rep = analyze(
    static_regime_input=StaticRegimeInput(time_varying_magnetic_field=True),
    magnetic_flux_input=MagneticFluxInput(b_field_t=0.1, loop_area_m2=0.05, n_turns=1),
    faraday_emf_input=FaradayEMFInput(n_turns=1, dflux_dt_weber_per_s=2e-4),
    lumped_inductor_input=None,
)
print("EMF (V):", rep.faraday_emf.emf_volts)
```

### Example — lumped inductor only (L5 focus)

```python
from em_induction import analyze, LumpedInductorInput, MagneticFluxInput, StaticRegimeInput

rep = analyze(
    static_regime_input=StaticRegimeInput(),
    magnetic_flux_input=MagneticFluxInput(b_field_t=0.0, loop_area_m2=1e-6),
    faraday_emf_input=None,
    lumped_inductor_input=LumpedInductorInput(inductance_h=1e-3, di_dt_a_per_s=200.0),
)
print("L dI/dt EMF (V):", rep.lumped_inductor.emf_volts)
```

### Example — minimal Faraday with only dΦ/dt

```python
from em_induction import analyze, FaradayEMFInput

rep = analyze(
    faraday_emf_input=FaradayEMFInput(n_turns=1, dflux_dt_weber_per_s=-0.03),
    lumped_inductor_input=None,
)
print(rep.faraday_emf.emf_volts)
```

---

## License

MIT — [LICENSE](LICENSE)
