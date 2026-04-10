from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SIG = ROOT / "SIGNATURE.sha256"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    failed = 0
    ok = 0
    for line in SIG.read_text(encoding="utf-8").splitlines():
        digest, rel = line.split("  ", 1)
        path = ROOT / rel
        if not path.exists():
            print(f"FAIL     {rel}")
            failed += 1
            continue
        got = sha256_file(path)
        if got != digest:
            print(f"FAIL     {rel}")
            failed += 1
        else:
            print(f"OK       {rel}")
            ok += 1
    print(f"\n{ok} ok, {failed} fail")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
