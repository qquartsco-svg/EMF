> **English.** Korean (정본): [README.md](README.md)

# EMF — Electromagnetic Induction Foundation `v0.1.0`

**Electromotive force (EMF) and magnetic induction** as **L1–L5 screening layers** aligned with Feynman *Lectures on Physics* **Vol. II, roughly Ch.16–17**. The public repo name **EMF** is a short label for that theme.

**Core:** the textbook Faraday form **ℰ = − N dΦ/dt** (SI) and the circuit idiom **V = −L dI/dt** as **pedagogical proxies**. This is **not** a replacement for **FDTD, SPICE, or full Maxwell solvers**.

**Korean canonical:** [README.md](README.md) · Curriculum map: [docs/FEYNMAN_VOL2_LAYER_MAP_EN.md](docs/FEYNMAN_VOL2_LAYER_MAP_EN.md)

---

## Contents

| Section | Topic |
|---------|--------|
| [Concept](#1-concept-emf-and-layers) | EMF, flux, Faraday, flux-rule caveats |
| [Layers](#2-layers-l1l5) | L1–L5 summary |
| [Extensibility](#3-extensibility-and-use) | Bridges, place in 00_BRAIN |
| [Security](#4-security-and-integrity) | SHA-256 manifest, limits |
| [Roadmap](#5-roadmap) | Possible extensions vs out-of-scope |
| [Quick start](#6-quick-start) | Install, tests, demo |

---

## 1. Concept (EMF and layers)

- **EMF:** in the Feynman Ch.17 narrative, the line integral of tangential force per unit charge around a conducting loop. Pure **electrostatics** usually gives a **conservative** **E** and **zero** circulation; **changing flux**, **motion**, **chemical sources**, etc. motivate **non-conservative** pieces and **induced EMF**.
- **Flux Φ:** L2 uses a **uniform B, flat loop** toy: **Φ = NBAcosθ**.
- **Faraday:** L3 implements **ℰ = −N dΦ/dt**.
- **Flux-rule pedagogy:** L4 flags setups where **defining the surface bounded by the loop** needs care (Feynman §17–2 style).

Longer concept: [CONCEPT_EN.md](CONCEPT_EN.md)

---

## 2. Layers (L1–L5)

| Layer | Role |
|-------|------|
| **L1** | Flags for ∂B/∂t, loop deformation, chemical EMF → **electrostatic-story** validity |
| **L2** | **Magnetic flux** (uniform-B toy) |
| **L3** | **Faraday EMF** |
| **L4** | **Flux-rule** subtlety hints |
| **L5** | **Lumped** V = −L dI/dt |

---

## 3. Extensibility and use

- **`ecosystem_bridges`:** when sibling `_staging` folders exist, shallow hooks to **`01_A`**, **`Atmospheric_Electric_Circuit`**, and **Optics** (via EM boundary).
- **Upstream:** electrostatics belongs primarily in **`Electromagnetic_Boundary_Foundation`** (its README points here for Ch.16–17).
- **Downstream:** multi-phase media, transformer detail, **mutual inductance matrices**, FDTD — expect **separate** engines/tools.
- **Pedagogy:** `omega_em` / `verdict` are **observer-style** checks, not final physics verdicts.

---

## 4. Security and integrity

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

## 5. Roadmap

**In-repo extensions that may fit:**

- Motional EMF (**v×B**) side-by-side with flux rule, same inputs
- **Two-coil** mutual-inductance toy
- More sibling bridges (e.g. frequency / MR foundations)

**Out of scope (separate projects):**

- Maxwell **FDTD/FEM**, **SPICE-class** simulation
- Hysteresis, radiation, full magnetostatics solvers

---

## 6. Quick start

| Item | Value |
|------|-------|
| Python | `>=3.10` |
| Tests | **5 passed** with local `pytest` (may change) |
| Deps | stdlib-first · dev: `pytest>=8.0` |

```bash
git clone https://github.com/qquartsco-svg/EMF.git
cd EMF
pip install -e ".[dev]"
pytest tests/
python3 examples/run_em_induction_demo.py
```

```python
from em_induction import analyze, FaradayEMFInput

rep = analyze()
print(rep.faraday_emf.emf_volts, rep.disclaimer)

rep2 = analyze(
    faraday_emf_input=FaradayEMFInput(n_turns=1, dflux_dt_weber_per_s=-0.03),
    lumped_inductor_input=None,
)
print(rep2.faraday_emf.emf_volts)
```

---

## License

MIT — [LICENSE](LICENSE)
