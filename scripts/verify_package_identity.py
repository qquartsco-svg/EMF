from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    ".gitignore",
    "BLOCKCHAIN_INFO.md",
    "BLOCKCHAIN_INFO_EN.md",
    "CONCEPT.md",
    "CONCEPT_EN.md",
    "LICENSE",
    "README.md",
    "README_EN.md",
    "VERSION",
    "pyproject.toml",
    "em_induction/__init__.py",
    "em_induction/contracts.py",
    "em_induction/static_regime.py",
    "em_induction/magnetic_flux.py",
    "em_induction/faraday_emf.py",
    "em_induction/flux_rule_pedagogy.py",
    "em_induction/lumped_inductor.py",
    "em_induction/foundation.py",
    "em_induction/ecosystem_bridges.py",
    "docs/FEYNMAN_VOL2_LAYER_MAP.md",
    "docs/FEYNMAN_VOL2_LAYER_MAP_EN.md",
    "examples/run_em_induction_demo.py",
    "tests/conftest.py",
    "tests/test_em_induction.py",
    "scripts/generate_signature.py",
    "scripts/verify_signature.py",
    "scripts/verify_package_identity.py",
    "scripts/release_check.py",
    "scripts/cleanup_generated.py",
]


def main() -> int:
    missing = 0
    for rel in REQUIRED:
        path = ROOT / rel
        if path.exists():
            print(f"OK — {rel}")
        else:
            print(f"MISSING — {rel}")
            missing += 1
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
