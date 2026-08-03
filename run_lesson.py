#!/usr/bin/env python3
"""
Lesson Runner for the 50-Lesson Python Adventure Game Curriculum.

By default it opens a fully interactive menu — just run it:

    python run_lesson.py

You can also drive it directly from the command line:

    python run_lesson.py 13          Run lesson 13 (show + test), then exit
    python run_lesson.py --all       Run every lesson's tests at once
    python run_lesson.py --progress  Show your progress and badges
    python run_lesson.py --reset     Reset progress + lesson files (prompts)
    python run_lesson.py --reset --yes   Reset without the confirmation prompt

Inside the interactive menu:

    n        Continue / retry the current lesson
    a        Run ALL lesson tests
    s        Show progress
    b        Show the badge wall (earned + locked)
    p <num>  Re-open a completed lesson (e.g. p 7)
    i <num>  Preview any lesson (e.g. i 20)
    h / ?    This help screen
    r        Reset everything
    q        Quit

The runner grades by running YOUR code. A lesson with no code yet is
skipped, not failed — red tests mean "try again", not "broken". See
GLOSSARY.md for every term and README.md for the parent guide.
"""

import argparse
import importlib.util
import json
import os
import re
import shutil
import sys
import time
import traceback
from pathlib import Path


# ============================
# Simple Color class for terminal output
# ============================

class Color:
    """ANSI color codes for terminal output."""
    RESET = "\033[0m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    DIM = "\033[2m"


# Directory paths
BASE_DIR = Path(__file__).parent
LESSONS_DIR = BASE_DIR / "lessons"
TESTS_DIR = BASE_DIR / "tests"
SCAFFOLDS_DIR = BASE_DIR / "scaffolds"
PROGRESS_FILE = BASE_DIR / "progress.json"

# Badges and their requirements
BADGES = {
    "variables_master": {"name": "Variables Master", "emoji": "📊", "range": (1, 3)},
    "loop_wizard": {"name": "Loop Wizard", "emoji": "🔄", "range": (11, 13)},
    "function_pro": {"name": "Function Pro", "emoji": "🔧", "range": (14, 16)},
    "class_creator": {"name": "Class Creator", "emoji": "🏗️", "range": (19, 23)},
    "file_handler": {"name": "File Handler", "emoji": "📁", "range": (25, 27)},
    "hero_builder": {"name": "Hero Builder", "emoji": "⚔️", "range": (31, 36)},
    "combat_master": {"name": "Combat Master", "emoji": "⚔️", "range": (37, 40)},
    "shop_keeper": {"name": "Shop Keeper", "emoji": "🏪", "range": (41, 43)},
    "game_designer": {"name": "Game Designer", "emoji": "🎮", "range": (44, 50)},
    "adventure_complete": {"name": "Adventure Complete", "emoji": "🏆", "range": (50, 50)},
}

TOTAL_LESSONS = 50

# A section header is an all-caps title sitting at column 0, e.g. "NEW WORDS".
SECTION_RE = re.compile(r"^([A-Z][A-Z0-9 &'/.-]+)$")


def load_progress():
    """Load student progress from progress.json."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {
        "current_lesson": 1,
        "completed": [],
        "badges": [],
        "total_time_minutes": 0,
        "streak_days": 0,
    }


def save_progress(progress):
    """Save student progress to progress.json."""
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def check_badges(progress):
    """Check and award badges based on completed lessons."""
    completed = set(progress["completed"])
    new_badges = []
    for badge_key, badge_info in BADGES.items():
        start, end = badge_info["range"]
        badge_lessons = set(range(start, end + 1))
        if badge_lessons.issubset(completed) and badge_key not in progress["badges"]:
            progress["badges"].append(badge_key)
            new_badges.append(badge_info)
    return new_badges


# ============================
# Output helpers
# ============================

def print_header(text, emoji="📚"):
    """Print a decorative header."""
    width = 60
    border = "=" * width
    print(f"\n{emoji} {Color.BOLD}{text}{Color.RESET}")
    print(border)


def print_success(text):
    """Print a success message in green."""
    print(f"  {Color.GREEN}✅ {text}{Color.RESET}")


def print_error(text):
    """Print an error message in red."""
    print(f"  {Color.RED}❌ {text}{Color.RESET}")


def print_hint(text):
    """Print a hint message in yellow."""
    print(f"  {Color.YELLOW}💡 {text}{Color.RESET}")


def print_warning(text):
    """Print a warning message in yellow."""
    print(f"  {Color.YELLOW}⚠️  {text}{Color.RESET}")


def print_badge(badge_info):
    """Print a badge award message."""
    print(f"\n  🎉 {Color.BOLD}BADGE EARNED:{Color.RESET} "
          f"{badge_info['emoji']} {badge_info['name']}")


# ============================
# Lesson / scaffold parsing
# ============================

def _docstring_bounds(source):
    """Locate the leading module docstring, allowing a string prefix.

    Lessons that teach escape sequences use a raw docstring (r\"\"\"...\"\"\") so
    that \\n and \\t appear literally in the instructions. Returns
    (body_start, close_start) or None when there is no docstring.
    """
    stripped = source.lstrip()
    offset = len(source) - len(stripped)
    prefix = 0
    while prefix < 2 and prefix < len(stripped) and stripped[prefix] in "rRbBuUfF":
        prefix += 1
    for quote in ('"""', "'''"):
        if stripped[prefix:].startswith(quote):
            body_start = offset + prefix + 3
            close_start = source.find(quote, body_start)
            if close_start == -1:
                return None
            return body_start, close_start
    return None


def lesson_file_for(lesson_num):
    """Return the path of lesson <n>'s file, or None when it doesn't exist."""
    matches = list(LESSONS_DIR.glob(f"{lesson_num:02d}_*.py"))
    return matches[0] if matches else None


def parse_lesson_docstring(text):
    """Split a lesson's instruction docstring into a title and named sections.

    Returns (title, sections) where ``sections`` maps a section name
    (e.g. "YOUR TASK") to its raw body text. Section headers are all-caps
    lines at column 0; everything else belongs to the current section.
    """
    title = None
    sections = {}
    current = None
    buffer = []
    started = False
    for line in text.splitlines():
        if not started:
            if line.strip():
                title = line.strip()
                started = True
            continue
        # Skip the decorative "====" underline that follows the title.
        if set(line.strip()) == {"="} and line.strip():
            continue
        match = SECTION_RE.match(line)
        if match:
            if current is not None:
                sections[current] = "\n".join(buffer).strip("\n")
            current = match.group(1).title()
            buffer = []
        elif current is not None:
            buffer.append(line)
    if current is not None:
        sections[current] = "\n".join(buffer).strip("\n")
    return title or "Lesson", sections


def render_lesson(lesson_num):
    """Display a lesson's instructions with the sections clearly laid out.

    The 8 sections are colour-coded, and each numbered step in YOUR TASK
    is highlighted so the student always knows the next concrete action.
    """
    lesson_path = lesson_file_for(lesson_num)
    if lesson_path is None:
        print_error(f"Lesson {lesson_num} not found!")
        return False

    content = lesson_path.read_text()
    bounds = _docstring_bounds(content)
    if bounds is None:
        print_header(f"Lesson {lesson_num}", "📚")
        print(content[:800])
        print("=" * 60)
        return True

    body_start, close_start = bounds
    title, sections = parse_lesson_docstring(content[body_start:close_start])

    print_header(title, "📚")
    for name, body in sections.items():
        if not name:
            continue
        # Headers are written UPPERCASE in the docstring; show them that way
        # rather than .title(), which mangles apostrophes (YOU'LL -> You'Ll).
        print(f"\n  {Color.BOLD}{Color.YELLOW}{name}{Color.RESET}")
        for line in body.splitlines():
            if re.match(r"^\s*Step\s+\d+:", line):
                # Highlight the numbered task the student should do next.
                print(f"  {Color.GREEN}{line}{Color.RESET}")
            else:
                print(f"  {line}")
    print(f"\n{Color.BOLD}{'=' * 60}{Color.RESET}")
    return True


def _check_lesson_compiles(lesson_num):
    """Return True if the lesson's source file compiles (or is absent)."""
    lesson_path = lesson_file_for(lesson_num)
    if lesson_path is None:
        return True
    try:
        with open(lesson_path, "r") as f:
            compile(f.read(), str(lesson_path), "exec")
    except SyntaxError as e:
        print_error(f"Lesson {lesson_num} has a syntax error: {e}")
        print_hint("Fix the red line in your editor, then run this lesson again.")
        return False
    return True


def _lesson_is_blank_scaffold(lesson_num):
    """Return True if the lesson file is still the unfilled starter template.

    After a reset the lesson file equals its scaffold: a shared instruction
    docstring plus a TODO marker and no student code. Such a file must never
    be counted as "completed" — its instruction docstring otherwise satisfies
    the keyword checks and fakes progress. We strip the leading docstring and
    confirm there is no real code beyond the scaffold TODO marker.
    """
    lesson_path = lesson_file_for(lesson_num)
    if lesson_path is None:
        return True  # no file at all -> nothing to complete
    try:
        source = lesson_path.read_text()
    except OSError:
        return True

    # Drop the leading module docstring (the shared instructions).
    bounds = _docstring_bounds(source)
    if bounds is not None:
        source = source[bounds[1] + 3:]

    # Ignore blank lines and the scaffold TODO marker; require real code.
    meaningful = [
        line
        for line in source.splitlines()
        if line.strip() and "TODO: Write your code for Lesson" not in line
    ]
    return len(meaningful) == 0


def _pytest_missing_message():
    """Print a friendly note when the tests can't import pytest."""
    print_error("This lesson's tests need pytest, which isn't installed here.")
    print_hint("Install it once with:   python3 -m pip install pytest")
    print_hint("Or run the whole curriculum with:   "
               "uv run --with pytest python run_lesson.py")


def run_lesson_tests_from_file(test_file, label=None):
    """Run every test_* function in the given test module file.

    Each test file is loaded by path (so names like test_capstone_game.py
    work), executed, and its test_* functions are run with friendly output.

    Grading semantics mirror pytest: an unattempted test (the lesson has no
    student code yet) is *skipped*, not failed; a wrong test *fails*. A
    lesson with zero attempted tests is reported as "not started" and is not
    counted as passed.
    """
    label = label or test_file.stem
    if not test_file.exists():
        print_hint(f"No tests found for {label}.")
        return True

    # If this test file belongs to a numbered lesson, check that lesson's
    # source file compiles before running (catches broken student code).
    stem = test_file.stem
    m = re.match(r"^test_(\d{2})$", stem)
    if m and not _check_lesson_compiles(int(m.group(1))):
        return False

    # Make the tests/ directory importable so shared helpers (e.g. _helpers)
    # resolve regardless of the current working directory.
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    spec = importlib.util.spec_from_file_location(stem, test_file)
    test_module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(test_module)
    except ModuleNotFoundError as e:
        # Almost always "No module named 'pytest'" — the student ran the
        # runner from a plain python3 without pytest installed.
        if "pytest" in str(e):
            _pytest_missing_message()
            return False
        print_error(f"Failed to load test file: {e}")
        traceback.print_exc()
        return False
    except Exception as e:  # noqa: BLE001 - surface any loader error plainly
        print_error(f"Failed to load test file: {e}")
        traceback.print_exc()
        return False

    test_functions = [
        (name, func)
        for name, func in vars(test_module).items()
        if name.startswith("test_") and callable(func)
    ]

    if not test_functions:
        print_hint("No test functions found in test file.")
        return True

    passed = failed = skipped = 0
    print(f"\n  {Color.BOLD}Running {len(test_functions)} test(s)...{Color.RESET}\n")

    for test_name, test_func in test_functions:
        try:
            test_func()
            print(f"  {Color.GREEN}✅ {test_name}{Color.RESET}")
            passed += 1
        except BaseException as e:
            # pytest.skip raises Skipped, which derives from BaseException.
            # Treat it as "not attempted" — never a pass, never a failure.
            if type(e).__name__ == "Skipped":
                print(f"  {Color.DIM}⏭️  {test_name}: skipped — {e}{Color.RESET}")
                skipped += 1
            else:
                raise
        except AssertionError as e:
            print(f"  {Color.RED}❌ {test_name}: {e}{Color.RESET}")
            failed += 1
        except Exception as e:  # noqa: BLE001 - report unexpected errors plainly
            print(f"  {Color.RED}❌ {test_name}: Unexpected error: {e}{Color.RESET}")
            failed += 1

    print()
    if failed > 0:
        print_hint(f"{failed} test(s) failed. Check your code and try again!")
        return False
    if skipped and passed == 0:
        # No student code attempted at all.
        return False
    if skipped:
        print_success(f"All {passed} attempted test(s) passed! "
                      f"({skipped} not started yet — write your code to try them.) 🎉")
    else:
        print_success("All tests passed! 🎉")
    return True


def run_lesson_tests(lesson_num):
    """Run tests for a specific lesson via run_lesson_tests_from_file."""
    return run_lesson_tests_from_file(
        TESTS_DIR / f"test_{lesson_num:02d}.py", label=f"Lesson {lesson_num}"
    )


# ============================
# Badges
# ============================

def next_badge(progress):
    """Return (key, info, remaining_count) for the badge to aim for next.

    "Next" means the earliest badge the student is actually working toward:
    prefer a badge whose lesson range includes the current lesson (you are in
    that arc); among those, the fewest lessons left; otherwise the earliest
    not-yet-earned badge ahead of you. This avoids announcing "Adventure
    Complete in 1 lesson" when the student is on lesson 17.
    """
    completed = set(progress["completed"])
    current = progress["current_lesson"]
    in_range, ahead = [], []
    for key, info in BADGES.items():
        if key in progress["badges"]:
            continue
        start, end = info["range"]
        remaining = set(range(start, end + 1)) - completed
        entry = (key, info, len(remaining))
        if start <= current <= end:
            # You are inside this badge's lesson arc and haven't earned it.
            in_range.append(entry)
        else:
            ahead.append(entry)
    pool = in_range or ahead
    if not pool:
        return None
    if in_range:
        # Inside an arc: aim for the one with the fewest lessons left.
        pool.sort(key=lambda e: e[2])
    else:
        # Not yet in any arc: aim for the earliest arc you'll reach.
        pool.sort(key=lambda e: BADGES[e[0]]["range"][0])
    return pool[0]


def render_badge_panel(progress, full=False):
    """Show earned badges, the next badge to aim for, and (if full) the wall."""
    earned = progress["badges"]
    if earned:
        line = "  ".join(
            f"{BADGES[k]['emoji']} {BADGES[k]['name']}"
            for k in earned if k in BADGES
        )
        print(f"\n  {Color.BOLD}Badges earned ({len(earned)}):{Color.RESET} {line}")
    else:
        print(f"\n  {Color.DIM}No badges yet — complete lessons to earn them!{Color.RESET}")

    nxt = next_badge(progress)
    if nxt:
        key, info, remaining = nxt
        start, end = info["range"]
        span = f"{start}" if start == end else f"{start}-{end}"
        print(f"  {Color.CYAN}Next badge: {info['emoji']} {info['name']} "
              f"in {remaining} lesson(s) (finish {span}){Color.RESET}")

    if full:
        print(f"\n  {Color.BOLD}All badges:{Color.RESET}")
        for key, info in BADGES.items():
            start, end = info["range"]
            span = f"{start}" if start == end else f"{start}-{end}"
            if key in earned:
                status = f"{info['emoji']} {Color.GREEN}EARNED{Color.RESET}"
            else:
                status = f"🔒 {Color.DIM}locked (lessons {span}){Color.RESET}"
            print(f"    {info['emoji'] if key in earned else '🔒'} "
                  f"{info['name']:<18} — {status}")


def render_compass(progress):
    """A one-line "where am I / what's next" banner for the menu."""
    current = progress["current_lesson"]
    parts = []
    if current <= TOTAL_LESSONS:
        parts.append(f"Lesson {current} now")
        if current + 1 <= TOTAL_LESSONS:
            parts.append(f"then {current + 1}")
    nxt = next_badge(progress)
    if nxt:
        parts.append(f"next badge: {nxt[1]['emoji']} {nxt[1]['name']} in {nxt[2]}")
    if parts:
        print(f"  {Color.CYAN}{' · '.join(parts)}{Color.RESET}")


def press_enter():
    """Prompt to continue, tolerating non-interactive (closed stdin) use."""
    try:
        input("Press Enter to continue...")
    except (EOFError, KeyboardInterrupt):
        print()


def show_help():
    """Print the in-runner help screen."""
    print_header("How to use this runner", "❓")
    print(f"""
  {Color.BOLD}Menu keys{Color.RESET}
    n         Work on / retry the current lesson
    a         Run EVERY lesson's tests at once
    s         Show your progress
    b         Show the badge wall (earned + locked)
    p <num>   Re-open a completed lesson (e.g. p 7)
    i <num>   Preview any lesson (e.g. i 20)
    h / ?     This help screen
    r         Reset all progress and lesson files
    q         Quit

  {Color.BOLD}Each lesson has 8 parts{Color.RESET}
    WHAT YOU'LL LEARN · NEW WORDS · HOW IT WORKS · YOUR TASK · EXAMPLE ·
    WHEN IT WORKS YOU'LL SEE · IF YOU GET STUCK · CHECK YOUR WORK

  {Color.BOLD}How grading works{Color.RESET}
    Write your code below the "{Color.GREEN}# TODO{Color.RESET}" line in
    lessons/<num>_*.py, then run this lesson. Tests run YOUR code — a red
    test means "{Color.YELLOW}try again{Color.RESET}", not "broken". A lesson with no
    code yet is skipped, never failed. Every error is explained in that
    lesson's "{Color.YELLOW}IF YOU GET STUCK{Color.RESET}" section, and every new word is
    defined in GLOSSARY.md.
""")


# ============================
# Lesson / progress actions
# ============================

def run_lesson(lesson_num):
    """Run a single lesson: show instructions, run tests, track progress."""
    if lesson_num < 1 or lesson_num > TOTAL_LESSONS:
        print_error(f"Lesson {lesson_num} not found. Lessons are 1-{TOTAL_LESSONS}.")
        return

    progress = load_progress()
    start_time = time.time()

    if not render_lesson(lesson_num):
        return

    success = run_lesson_tests(lesson_num)

    elapsed = (time.time() - start_time) / 60
    progress["total_time_minutes"] += elapsed

    # Reset guard: a lesson file that is still the unfilled starter template
    # must not be marked complete. Its shared instruction docstring would
    # otherwise satisfy the keyword checks and fake progress, so a reset could
    # march the student straight through every lesson without writing code.
    if not success or _lesson_is_blank_scaffold(lesson_num):
        if _lesson_is_blank_scaffold(lesson_num):
            print_warning(
                f"Lesson {lesson_num} is still the starter template — "
                f"write your code in {lesson_file_for(lesson_num).name}, then run it again."
            )
        save_progress(progress)
        return

    if lesson_num not in progress["completed"]:
        progress["completed"].append(lesson_num)
        print_success(f"Lesson {lesson_num} completed! Added to your progress.")

    progress["current_lesson"] = lesson_num + 1

    new_badges = check_badges(progress)
    for badge in new_badges:
        print_badge(badge)

    if lesson_num < TOTAL_LESSONS:
        print_hint(f"Next: python run_lesson.py {lesson_num + 1}")
    else:
        print_badge(BADGES["adventure_complete"])

    save_progress(progress)


def render_progress_bar(progress, label="Progress"):
    """Render a progress bar and summary line."""
    completed = progress["completed"]
    completed_count = len(completed)
    bar_width = 40
    filled = int(bar_width * completed_count / TOTAL_LESSONS)
    bar = "█" * filled + "░" * (bar_width - filled)
    completed_summary = ""
    if completed:
        completed_summary = (f"\n\n  Completed lessons: "
                             f"{', '.join(str(l) for l in sorted(completed))}\n")
    next_lesson = progress["current_lesson"]
    next_summary = ""
    if next_lesson <= TOTAL_LESSONS:
        next_summary = (f"\n  Next lesson: {next_lesson}\n"
                        f"  Run: python run_lesson.py {next_lesson}\n")
    summary = (
        f"\n  {label}: [{bar}] {completed_count}/{TOTAL_LESSONS}\n"
        f"  Time spent: {progress['total_time_minutes']:.1f} minutes\n"
        f"  Streak: {progress['streak_days']} days"
        f"{completed_summary}"
        f"{next_summary}"
    )
    print(summary)


def show_progress():
    """Display the student's progress."""
    progress = load_progress()
    print_header("Your Progress", "📊")
    render_progress_bar(progress, label="Progress")
    render_badge_panel(progress)


def reset_progress(force: bool = False):
    """Reset progress and restore lesson files from scaffold templates.

    Guards: refuses to reset if any scaffold file fails to compile, so a
    corrupt template can never be copied into lessons/ and leave the
    student stuck.

    Args:
        force: when True, skip the interactive confirmation prompt. Use the
            CLI `--reset --yes` path; the interactive menu always prompts.
    """
    # Guard: never reset if a scaffold is broken (would corrupt lessons/).
    broken = []
    for sc in sorted(SCAFFOLDS_DIR.glob("*.py")):
        try:
            compile(sc.read_text(), str(sc), "exec")
        except SyntaxError as e:
            broken.append(f"{sc.name}: {e}")
    if broken:
        print_error("Refusing to reset: scaffold files are broken:")
        for b in broken:
            print_error(b)
        print_warning("Fix the files in scaffolds/ before resetting.")
        return

    if not force:
        print_warning("This will reset all progress and lesson files.")
        confirm = input("Are you sure? (y/n): ").strip().lower()
        if confirm != "y":
            print("Reset cancelled.")
            return

    # Reset lesson files back to scaffold templates
    copied = 0
    for scaffold_file in SCAFFOLDS_DIR.glob("*.py"):
        dest = LESSONS_DIR / scaffold_file.name
        if dest.exists():
            dest.unlink()
        shutil.copy(scaffold_file, dest)
        copied += 1
    if copied:
        print_success(f"Restored {copied} lesson files from scaffolds/.")

    if PROGRESS_FILE.exists():
        PROGRESS_FILE.unlink()
    save_progress({
        "current_lesson": 1,
        "completed": [],
        "badges": [],
        "total_time_minutes": 0,
        "streak_days": 0,
    })
    print_header("Full Reset Complete!", "🔄")
    print_success("Progress cleared.")
    print_success("All lesson files reset to starter templates.")
    print("Starting fresh from lesson 1!")


def run_all_tests():
    """Run all lesson tests. Returns True if every suite passed."""
    print_header("Running All Tests", "🧪")
    all_passed = True
    test_files = sorted(TESTS_DIR.glob("test_*.py"))
    for test_file in test_files:
        if not test_file.exists():
            continue
        print(f"\n  {Color.BOLD}{test_file.stem}:{Color.RESET}")
        if not run_lesson_tests_from_file(test_file):
            all_passed = False
    if all_passed:
        print_success("\nAll tests passed! 🎉")
    else:
        print_error("\nSome tests failed. Review the output above.")
    return all_passed


# ============================
# Interactive loop
# ============================

def interactive_loop():
    """Interactive menu: the default way to drive the runner.

    Auto-opens the current lesson when it isn't finished, otherwise shows the
    menu with the progress compass and badge panel always visible.
    """
    while True:
        progress = load_progress()
        current = progress["current_lesson"]
        completed = progress["completed"]

        # Auto-open current lesson if not finished yet
        if current <= TOTAL_LESSONS and current not in completed:
            print_header("Python Adventure Curriculum", "🎮")
            completed_count = len(completed)
            bar_width = 40
            filled = int(bar_width * completed_count / TOTAL_LESSONS)
            bar = "█" * filled + "░" * (bar_width - filled)
            print(f"\n  Progress: [{bar}] {completed_count}/{TOTAL_LESSONS}")
            print(f"  Time: {progress['total_time_minutes']:.1f} min | "
                  f"Streak: {progress['streak_days']} days")
            render_badge_panel(progress)
            print()
            run_lesson(current)
            press_enter()
            continue

        # All lessons done or current is completed — show menu
        if current > TOTAL_LESSONS:
            print_header("Python Adventure Curriculum", "🏆")
            print_success("All lessons completed! You are a Python Hero!")
            print_badge(BADGES["adventure_complete"])
        else:
            print_header("Your Curriculum Menu", "🎮")
            render_progress_bar(progress, label="Progress")
            render_badge_panel(progress)
            render_compass(progress)

        print("\n  Menu:")
        print(f"    {Color.GREEN}n{Color.RESET} - Continue / retry current lesson ({current})")
        print(f"    {Color.CYAN}a{Color.RESET} - Run ALL lesson tests")
        print(f"    {Color.BLUE}s{Color.RESET} - Show progress")
        print(f"    {Color.MAGENTA}b{Color.RESET} - Show the badge wall")
        completed_rev = sorted(completed, reverse=True)[:8]
        if completed_rev:
            print(f"    {Color.CYAN}p <num>{Color.RESET} - Re-open a completed lesson: "
                  f"{', '.join(str(x) for x in completed_rev)}")
        print(f"    {Color.YELLOW}i <num>{Color.RESET} - Preview any lesson")
        print(f"    {Color.BOLD}h / ?{Color.RESET} - Help")
        print(f"    {Color.MAGENTA}r{Color.RESET} - Reset everything")
        print(f"    {Color.RED}q{Color.RESET} - Quit")

        try:
            choice = input("\nEnter choice: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if choice in ("q",):
            print("Goodbye!")
            break

        if choice in ("h", "?"):
            show_help()
            press_enter()
            continue

        if choice == "n":
            if current <= TOTAL_LESSONS:
                run_lesson(current)
            else:
                print_error("All lessons are complete! Use 'i <num>' to preview.")
            press_enter()
            continue

        if choice == "a":
            run_all_tests()
            press_enter()
            continue

        if choice == "s":
            show_progress()
            press_enter()
            continue

        if choice == "b":
            print_header("Badge Wall", "🏅")
            render_badge_panel(progress, full=True)
            press_enter()
            continue

        if choice == "r":
            reset_progress()
            press_enter()
            continue

        if choice.startswith("p ") and completed_rev:
            _open_lesson(completed, choice, run=True)
            press_enter()
            continue

        if choice.startswith("i "):
            _open_lesson(completed, choice, run=False)
            press_enter()
            continue

        print_error("Invalid option. Use n / a / s / b / p <num> / i <num> / h / r / q.")
        press_enter()


def _open_lesson(completed, choice, run):
    """Handle the `p <num>` (completed) and `i <num>` (preview) commands."""
    try:
        num = int(choice[2:].strip())
    except ValueError:
        print_error("Enter a valid lesson number.")
        return
    if run and num not in completed:
        print_error(f"Lesson {num} isn't completed yet. Use 'i {num}' to preview it.")
        return
    if run:
        run_lesson(num)
    else:
        render_lesson(num)
        print_hint("This is a lesson preview — your own code isn't changed.")


def main():
    """Main entry point.

    No arguments launches the interactive menu. A lesson number, --all,
    --progress, --reset run the matching action directly. All paths are
    resolved relative to this script, so the repo root is the working dir.
    """
    parser = argparse.ArgumentParser(
        description="50-Lesson Python Adventure Game curriculum runner."
    )
    parser.add_argument(
        "lesson", nargs="?", type=int,
        help="Run a specific lesson number and exit (e.g. 13).",
    )
    parser.add_argument(
        "--lesson", type=int, dest="lesson_flag",
        help="Alias for the positional lesson number.",
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Run every lesson's tests at once.",
    )
    parser.add_argument(
        "--progress", action="store_true",
        help="Show your progress and badges, then exit.",
    )
    parser.add_argument(
        "--reset", action="store_true",
        help="Reset all progress and lesson files to starter templates.",
    )
    parser.add_argument(
        "--yes", action="store_true",
        help="Skip the confirmation prompt (use together with --reset).",
    )
    args = parser.parse_args()

    os.chdir(BASE_DIR)

    if args.reset:
        reset_progress(force=args.yes)
        return

    number = args.lesson or args.lesson_flag
    if number is not None:
        run_lesson(number)
        return

    if args.all:
        run_all_tests()
        return

    if args.progress:
        show_progress()
        return

    interactive_loop()


if __name__ == "__main__":
    main()
