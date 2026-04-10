from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def run(*args: str) -> int:
    return subprocess.run(args, cwd=ROOT).returncode


def main() -> int:
    rc = 0
    rc |= run(sys.executable, "scripts/verify_package_identity.py")
    rc |= run(sys.executable, "scripts/verify_signature.py")
    rc |= run(sys.executable, "-m", "pytest", "tests", "-q")
    if rc == 0:
        print("OK")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
