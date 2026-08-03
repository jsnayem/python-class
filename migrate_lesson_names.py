"""One-shot migration: rename lesson files whose names describe the wrong topic.

Six lessons taught something other than what their filename said, e.g.
11_loops_intro.py actually teaches functions. This renames the scaffold, the
student's lesson file and the answer key together, and rewrites the
load_answer("...") references in the tests.

Usage:
    python migrate_lesson_names.py           # show what would change
    python migrate_lesson_names.py --apply
"""
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent

# old stem -> new stem, based on what each lesson actually teaches
RENAMES = {
    "11_loops_intro": "11_functions_spell",
    "12_while_loops": "12_default_arguments",
    "15_function_args": "15_dictionaries",
    "17_dictionaries": "17_classes",
    "19_classes_intro": "19_inheritance_intro",
    "22_methods": "22_subclasses",
}

TARGET_DIRS = ["scaffolds", "lessons", "answer_key"]


def plan():
    """Return the list of (path, new_path) renames that actually apply."""
    moves = []
    for old, new in RENAMES.items():
        for folder in TARGET_DIRS:
            src = ROOT / folder / f"{old}.py"
            if src.exists():
                moves.append((src, ROOT / folder / f"{new}.py"))
    return moves


def test_files_needing_rewrite():
    """Test files that mention a renamed answer-key module."""
    hits = []
    for path in sorted((ROOT / "tests").glob("test_*.py")):
        text = path.read_text()
        if any(f'"{old}"' in text for old in RENAMES):
            hits.append(path)
    return hits


def rewrite_tests(apply=False):
    changed = []
    for path in test_files_needing_rewrite():
        text = original = path.read_text()
        for old, new in RENAMES.items():
            text = text.replace(f'"{old}"', f'"{new}"')
        if text != original:
            changed.append(path)
            if apply:
                path.write_text(text)
    return changed


def migrate_progress(apply=False):
    """Progress is keyed by lesson number, so only stored names need fixing."""
    path = ROOT / "progress.json"
    if not path.exists():
        return False
    data = json.loads(path.read_text())
    text = json.dumps(data)
    if not any(old in text for old in RENAMES):
        return False
    for old, new in RENAMES.items():
        text = text.replace(old, new)
    if apply:
        path.write_text(json.dumps(json.loads(text), indent=2))
    return True


def main():
    apply = "--apply" in sys.argv
    moves = plan()
    tests = test_files_needing_rewrite()

    if apply:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup = ROOT / f"lessons_backup_{stamp}"
        shutil.copytree(ROOT / "lessons", backup)
        print(f"Backed up lessons/ to {backup.name}/")

    for src, dst in moves:
        print(f"{'RENAME' if apply else 'would rename'}: "
              f"{src.parent.name}/{src.name} -> {dst.name}")
        if apply:
            src.rename(dst)

    for path in tests:
        print(f"{'REWRITE' if apply else 'would rewrite'}: tests/{path.name}")
    rewrite_tests(apply=apply)

    if migrate_progress(apply=apply):
        print(f"{'UPDATED' if apply else 'would update'}: progress.json")

    print(f"\n{len(moves)} file(s), {len(tests)} test file(s).")
    if not apply:
        print("Dry run. Re-run with --apply to make the changes.")


if __name__ == "__main__":
    main()
