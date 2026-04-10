from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "SIGNATURE.sha256"


def wanted(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if path.is_dir():
        return False
    if rel.parts[0] in {".git", ".pytest_cache"}:
        return False
    if "__pycache__" in rel.parts:
        return False
    if path.suffix in {".pyc", ".pyo"}:
        return False
    if any(part.endswith(".egg-info") for part in rel.parts):
        return False
    return True


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    lines = []
    for path in sorted(p for p in ROOT.rglob("*") if wanted(p)):
        rel = path.relative_to(ROOT).as_posix()
        if rel == "SIGNATURE.sha256":
            continue
        lines.append(f"{sha256_file(path)}  {rel}")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Signed {len(lines)} files -> {OUT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
