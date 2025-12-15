from __future__ import annotations

import os
import sys
from pathlib import Path


def _ensure_src_on_path() -> None:
    repo_root = Path(__file__).resolve().parent
    os.chdir(repo_root)
    src = repo_root / "src"
    sys.path.insert(0, str(src))


def main() -> None:
    _ensure_src_on_path()
    from multi_agent.main import main as app_main

    app_main()


if __name__ == "__main__":
    main()
