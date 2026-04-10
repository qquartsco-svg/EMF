> **English.** Korean (정본): [FEYNMAN_VOL2_LAYER_MAP.md](FEYNMAN_VOL2_LAYER_MAP.md)

# Feynman lecture flow vs 00_BRAIN `_staging` (summary)

This table is **not** a full syllabus clone; it highlights what exists in-repo and **large gaps**.

## Volume I (reference)

| Topic (rough) | `_staging` example | Note |
|---------------|-------------------|------|
| Waves / oscillations | `Wave_Propagation_Foundation` | aligned in spirit |
| Mechanics / energy (broad) | ENGINE_HUB / many modules | not one monolithic “Vol I” package |

## Volume II — electromagnetism

| Feynman Vol.II (rough) | Layer / package | Inside `em_induction` |
|------------------------|-----------------|----------------------|
| Early: vector calculus, electrostatics | `01_A_Electromagnetic_Boundary_Foundation` | bridge (L1 static story) |
| Atmosphere, dielectric polarization | `Atmospheric_Electric_Circuit_Foundation` (Ch.9–10) | bridge |
| **Induced currents (Ch.16)** | **`Electromagnetic_Induction_Foundation`** | motivation + Faraday setup |
| **Laws of induction (Ch.17)** | **same package L3–L4** | EMF, flux rule, pedagogy |
| Lumped L, mutual inductance | **same package L5** | thin proxy |
| Maxwell equations, waves | (no FDTD-class engine here) | out of screening scope |

## Missing by design (or not yet)

- **3D Maxwell numerics** (FDTD, FEM)
- **Full magnetostatics** solvers
- **SPICE-class** circuit simulation

## Coherence checklist

1. Is electrostatics enough? → `em_induction` L1 + `01_A`
2. Is flux through a loop defined? → L2
3. Is ℰ = −N dΦ/dt appropriate? → L3
4. Sliding rod / contacts — **flux-rule subtlety**? → L4
5. Coil / dI/dt only? → L5
