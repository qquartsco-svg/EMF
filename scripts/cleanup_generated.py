from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TARGETS = [
    ROOT / ".pytest_cache",
    ROOT / "em_induction" / "__pycache__",
    ROOT / "tests" / "__pycache__",
    ROOT / "scripts" / "__pycache__",
]


def main() -> int:
    removed = 0
    for path in TARGETS:
        if path.exists():
            shutil.rmtree(path)
            print(f"Removed {path.relative_to(ROOT)}")
            removed += 1
    print(f"Cleaned {removed} paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
