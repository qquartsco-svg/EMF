> **English.** Korean (정본): [CONCEPT.md](CONCEPT.md)

# Electromagnetic Induction Foundation — Concept

## Role

A **screening stack** for **induction and EMF** in the spirit of Feynman **Vol. II, Ch.16–17**, after electrostatics / atmosphere / dielectrics (early Vol.II and Ch.9–10 elsewhere). It does **not** replace full Maxwell numerics or SPICE.

## Vol.I vs Vol.II (roughly in 00_BRAIN)

- **Vol.I**: mechanics, heat, waves spread across engines; e.g. `Wave_Propagation_Foundation` aligns with the waves narrative.
- **Vol.II**: `01_A` for electrostatic boundaries, `Atmospheric_Electric_Circuit` for Ch.9–10, **this package** for the Ch.16–17 layer.

Table: [docs/FEYNMAN_VOL2_LAYER_MAP_EN.md](docs/FEYNMAN_VOL2_LAYER_MAP_EN.md)

## Layers (this package)

| Layer | Role | Feynman anchor (approx.) |
|-------|------|---------------------------|
| L1 | When electrostatic / scalar-potential language is fair | flags for ∂B/∂t, motion, chemical EMF, … |
| L2 | Uniform **B**, flat loop: Φ = NBAcosθ | flux definition toy |
| L3 | ℰ = −N dΦ/dt | Ch.17 flux rule (screening) |
| L4 | **Caveats** to the flux rule | Ch.17–2 style pedagogy |
| L5 | Lumped V = −L dI/dt | circuit language after induction |

## Bridges

- `01_A_Electromagnetic_Boundary_Foundation`
- `Atmospheric_Electric_Circuit_Foundation`
- Optics via EM boundary when importable

## Disclaimer

Not a substitute for measurements, simulations, or textbooks. Ω and verdict are **pedagogical checks**.
