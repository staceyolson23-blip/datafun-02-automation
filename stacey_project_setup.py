"""
P2: Python Scripting & Automation — Stacey
Goal right now: get a minimal script to run.
"""

from pathlib import Path
from datetime import datetime

# Try to import your Module 1 tagline; fall back if it's not there yet.
try:
    from utils_stacey import get_tagline  # type: ignore
except Exception:
    try:
        from utils import get_tagline  # type: ignore
    except Exception:
        def get_tagline() -> str:
            return "Project Setup • (using fallback tagline)"

# --- Project paths ---
PROJECT_ROOT = Path(__file__).parent
DATA_DIR     = PROJECT_ROOT / "data"
REPORTS_DIR  = PROJECT_ROOT / "reports"
IMAGES_DIR   = PROJECT_ROOT / "images"
OUTPUTS_DIR  = PROJECT_ROOT / "outputs"
ARCHIVE_DIR  = PROJECT_ROOT / "archive"

DIRECTORIES = [DATA_DIR, REPORTS_DIR, IMAGES_DIR, OUTPUTS_DIR, ARCHIVE_DIR]

def ensure_dirs(dirs: list[Path]) -> list[Path]:
    """Create any missing directories and return the ones that were newly created."""
    created = [d for d in dirs if not d.exists()]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    return created

# Keep the rest simple for the first run 
def main() -> None:
    print(get_tagline())
    print("Hello from P2!")

    created = ensure_dirs(DIRECTORIES)
    if created:
        print("Created:", ", ".join(p.name for p in created))
    else:
        print("All expected folders already exist.")

if __name__ == "__main__":
    main()