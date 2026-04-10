# Electromagnetic Induction Foundation — SHA-256 integrity

- **Purpose:** verify that the **release file tree** matches recorded SHA-256 hashes.
- **Scope:** paths listed in `SIGNATURE.sha256` (README, CONCEPT, `em_induction`, tests, scripts, `VERSION`, …).
- **“Blockchain” wording:** this is an **integrity manifest**, not a cryptocurrency ledger.

Verification:

```bash
python3 scripts/generate_signature.py   # regenerate after changes
python3 scripts/verify_signature.py
python3 scripts/verify_package_identity.py
python3 scripts/release_check.py
```

**Security limits:** signatures check **file integrity**, not physical correctness, lab reproducibility, or malicious runtime behavior. Combine with **repository provenance, signed commits, and CI** for supply-chain confidence.
