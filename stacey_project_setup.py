"""
Author: Stacey Olson
Course: Data Analytics Fundamentals
Assignment: P2 — Python Scripting & Automation
Description: Practicing Chapters 3 & 4 (comprehensions, branching, try/except, file I/O).
I chose timestamped filenames so artifacts don’t get overwritten between runs.
"""

from pathlib import Path
from datetime import datetime
import random
import statistics
import json
import re

# Import Module 1 tagline
from utils_stacey import get_tagline

# --- Project paths ---
PROJECT_ROOT = Path(__file__).parent
DATA_DIR     = PROJECT_ROOT / "data"
REPORTS_DIR  = PROJECT_ROOT / "reports"
IMAGES_DIR   = PROJECT_ROOT / "images"
OUTPUTS_DIR  = PROJECT_ROOT / "outputs"
ARCHIVE_DIR  = PROJECT_ROOT / "archive"
DIRECTORIES  = [DATA_DIR, REPORTS_DIR, IMAGES_DIR, OUTPUTS_DIR, ARCHIVE_DIR]

def ensure_dirs(dirs: list[Path]) -> list[Path]:
    """
    Make sure my project folders exist.
    Why: I want a predictable layout so later scripts can rely on these paths.
    Returns: list of new directories created (so I can print a friendly message).
    """
    created = [d for d in dirs if not d.exists()]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    return created

def timestamp(fmt: str = "%Y-%m-%d_%H-%M-%S") -> str:
    """
    Return a filesystem-friendly timestamp string.
    Note: I prefer underscores instead of spaces/colons to avoid cross-platform issues.
    """
    return datetime.now().strftime(fmt)

def build_path(directory: Path, stem: str, ext: str) -> Path:
    """
    Build a timestamped filename like data/numbers_2025-09-06_22-27-42.csv.
    Reason: I don’t want to overwrite older runs while I’m iterating.
    """
    suffix = ext if ext.startswith(".") else f".{ext}"
    return directory / f"{stem}_{timestamp()}{suffix}"

def write_sample_csv(path: Path, rows: int = 12) -> Path:
    """
    Write a tiny CSV with n, n^2, n^3.

    Why this is here: quick practice with loops, f-strings, and file I/O.
    I keep it small so I can eyeball the file contents easily.
    """
    rows = max(1, int(rows))

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
    print("safe_divide(10, 0) ->", safe_divide(10, 0))
    print("categorize_number(7) ->", categorize_number(7))
    note_to_readme(
        "P2 Automation Functions Implemented",
        [
            "ensure_dirs(dirs) - create project folders if missing",
            "timestamp/build_path - timestamped artifact paths",
            "write_sample_csv(path, rows) - tiny CSV artifact",
            "generate_random_numbers - list comprehension",
            "summarize_numbers - list/set/dict comprehensions + stats",
            "dump_json - pretty JSON artifact",
            "safe_divide - try/except example",
            "categorize_number - if/elif/else example",
        ],
    )

def generate_random_numbers(n: int, low: int = 1, high: int = 100) -> list[int]:
    """
    Return a list of n random integers in [low, high].

    Intent: explicit list comprehension usage (required for this assignment).
    """
    return [random.randint(low, high) for _ in range(n)]  # list comprehension ✅

def summarize_numbers(nums: list[int]) -> dict:
    """
    Compute a quick numeric summary + comprehension practice.

    Choices:
      - list comps for evens/odds to practice filtering
      - set comp to count unique values
      - dict comp to map first 10 numbers → squares (small, inspectable slice)
      - statistics: I’m using *population* stdev (pstdev) here on purpose
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
    """
    Write a dict to pretty JSON.
    I sort keys so diffs are stable in Git, which makes code reviews cleaner.
    """
    path.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
    return path

def safe_divide(a: float, b: float) -> float | None:
    """
    Return a/b, or None if b == 0.
    Why None: I’d rather return a sentinel than explode my script for this demo.
    In a bigger app I might raise a ValueError and let the caller decide.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None

def categorize_number(x: int) -> str:
    """Return 'negative', 'zero', or 'positive' (demo if/elif/else)."""
    if x < 0:
        return "negative"
    elif x == 0:
        return "zero"
    else:
        return "positive"
    
def note_to_readme(section_title: str, lines: list[str]) -> None:
    """
    Keep a single auto-maintained notes block in README.md.
    My rule: replace between AUTO_NOTES markers if they exist; otherwise add them.
    This keeps my README from growing duplicates every time I run the script.
    """
    readme = PROJECT_ROOT / "README.md"
    start = "<!-- AUTO_NOTES_START -->"
    end   = "<!-- AUTO_NOTES_END -->"

    section = "\n".join(
        ["", f"## {section_title}", ""] + [f"- {ln}" for ln in lines] + ["", ""]
    )

    text = readme.read_text(encoding="utf-8") if readme.exists() else f"# {PROJECT_ROOT.name}\n\n"

    if start in text and end in text:
        # replace existing block
        pattern = re.compile(re.escape(start) + r"[\s\S]*?" + re.escape(end))
        new_text = pattern.sub(f"{start}\n{section}{end}", text, count=1)
    else:
        # add new block at the end
        new_text = text + f"\n{start}\n{section}{end}\n"

    readme.write_text(new_text, encoding="utf-8")

if __name__ == "__main__":
    main()