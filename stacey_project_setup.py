"""
P2: Python Scripting & Automation — Stacey
Goal right now: folders + a tiny CSV.
"""

from pathlib import Path
from datetime import datetime
import random
import statistics
import json

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
DIRECTORIES  = [DATA_DIR, REPORTS_DIR, IMAGES_DIR, OUTPUTS_DIR, ARCHIVE_DIR]

def ensure_dirs(dirs: list[Path]) -> list[Path]:
    """Create any missing directories and return the ones that were newly created."""
    created = [d for d in dirs if not d.exists()]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    return created

def timestamp(fmt: str = "%Y-%m-%d_%H-%M-%S") -> str:
    return datetime.now().strftime(fmt)

def build_path(directory: Path, stem: str, ext: str) -> Path:
    suffix = ext if ext.startswith(".") else f".{ext}"
    return directory / f"{stem}_{timestamp()}{suffix}"

def write_sample_csv(path: Path, rows: int = 12) -> Path:
    header = "n,square,cube"
    lines = [header]
    for n in range(1, rows + 1):
        lines.append(f"{n},{n**2},{n**3}")
    path.write_text("\n".join(lines), encoding="utf-8")
    return path

def main() -> None:
    print(get_tagline())
    print("Hello from P2!")

    # 1) Ensure folders exist
    created = ensure_dirs(DIRECTORIES)
    if created:
        print("Created:", ", ".join(p.name for p in created))
    else:
        print("All expected folders already exist.")

    # 2) Build a timestamped path and write a tiny CSV to data/
    csv_path = build_path(DATA_DIR, "numbers", "csv")
    write_sample_csv(csv_path, rows=12)
    print(f"Wrote CSV -> {csv_path.relative_to(PROJECT_ROOT)}")

    # 3) Generate random numbers, summarize, and write JSON to outputs/
    nums = generate_random_numbers(50, 1, 100)
    summary = summarize_numbers(nums)
    json_path = build_path(OUTPUTS_DIR, "numbers_summary", "json")
    dump_json(summary, json_path)
    print(f"Wrote JSON -> {json_path.relative_to(PROJECT_ROOT)}")

def generate_random_numbers(n: int, low: int = 1, high: int = 100) -> list[int]:
    """Return a list of n random integers in [low, high]."""
    return [random.randint(low, high) for _ in range(n)]  # list comprehension ✅

def summarize_numbers(nums: list[int]) -> dict:
    """
    Return summary stats + comprehension practice.
      - evens (list comp)
      - odds (list comp)
      - unique values (set comp)
      - squares (dict comp for first 10 numbers)
    """
    evens = [x for x in nums if x % 2 == 0]
    odds  = [x for x in nums if x % 2 != 0]
    unique_vals = {x for x in nums}                # set comp ✅
    squares_map = {x: x**2 for x in nums[:10]}     # dict comp ✅

    mean   = statistics.mean(nums) if nums else None
    median = statistics.median(nums) if nums else None
    stdev  = statistics.pstdev(nums) if len(nums) > 1 else None

    return {
        "count": len(nums),
        "min": min(nums) if nums else None,
        "max": max(nums) if nums else None,
        "mean": mean,
        "median": median,
        "stdev": stdev,
        "evens_count": len(evens),
        "odds_count": len(odds),
        "unique_count": len(unique_vals),
        "sample_squares": squares_map,
    }


def dump_json(obj: dict, path: Path) -> Path:
    """Write a dict to pretty JSON."""
    path.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
    return path

if __name__ == "__main__":
    main()