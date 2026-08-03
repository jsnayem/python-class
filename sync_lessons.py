"""Refresh lesson instructions from the scaffolds without losing student code.

A lesson file is a scaffold docstring followed by the student's own code.
When the instructions are improved, students should get the new wording
without having their work deleted.

Usage:
    python sync_lessons.py           # show what would change
    python sync_lessons.py --apply   # actually rewrite lessons/
"""
import shutil
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
LESSONS_DIR = ROOT / "lessons"
SCAFFOLDS_DIR = ROOT / "scaffolds"
TOTAL_LESSONS = 50
TODO_MARKER = "# TODO: Write your code for Lesson"


def docstring_bounds(source):
    """Locate the leading module docstring, allowing an r/b/u/f prefix.

    Returns (start, end) index of the whole docstring including quotes, or
    None when the file has no leading docstring.
    """
    stripped = source.lstrip()
    offset = len(source) - len(stripped)
    prefix = 0
    while prefix < 2 and prefix < len(stripped) and stripped[prefix] in "rRbBuUfF":
        prefix += 1
    for quote in ('"""', "'''"):
        if stripped[prefix:].startswith(quote):
            start = offset + prefix
            end = source.find(quote, start + prefix + 3)
            if end == -1:
                return None
            return start, end + 3
    return None


def split_lesson(source):
    """Return (instructions, student_code) for a lesson file."""
    bounds = docstring_bounds(source)
    if bounds is None:
        return "", source
    return source[: bounds[1]], source[bounds[1] :]


def student_has_written_code(body):
    """True when the part below the docstring contains real code."""
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith(TODO_MARKER):
            continue
        return True
    return False


def sync(apply=False):
    changed, preserved, skipped = [], [], []
    for num in range(1, TOTAL_LESSONS + 1):
        scaffolds = sorted(SCAFFOLDS_DIR.glob(f"{num:02d}_*.py"))
        lessons = sorted(LESSONS_DIR.glob(f"{num:02d}_*.py"))
        if not scaffolds or not lessons:
            skipped.append(num)
            continue

        scaffold_src = scaffolds[0].read_text()
        lesson_path = lessons[0]
        lesson_src = lesson_path.read_text()

        new_instructions, _ = split_lesson(scaffold_src)
        old_instructions, student_body = split_lesson(lesson_src)

        if old_instructions == new_instructions:
            continue

        if student_has_written_code(student_body):
            # Keep their work, only swap the instructions above it.
            new_src = new_instructions + student_body
            preserved.append(num)
        else:
            new_src = scaffold_src
        changed.append(num)

        if apply:
            lesson_path.write_text(new_src)

    return changed, preserved, skipped


def main():
    apply = "--apply" in sys.argv

    if apply and LESSONS_DIR.exists():
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup = ROOT / f"lessons_backup_{stamp}"
        shutil.copytree(LESSONS_DIR, backup)
        print(f"Backed up lessons/ to {backup.name}/")

    changed, preserved, skipped = sync(apply=apply)

    verb = "Updated" if apply else "Would update"
    print(f"{verb} {len(changed)} lesson(s).")
    if preserved:
        print(f"Student code preserved in lesson(s): {preserved}")
    if skipped:
        print(f"No matching file for lesson(s): {skipped}")
    if not apply:
        print("\nDry run. Re-run with --apply to write the changes.")


if __name__ == "__main__":
    main()
