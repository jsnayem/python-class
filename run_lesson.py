#!/usr/bin/env python3
"""
Lesson Runner for the 50-Lesson Python Adventure Game Curriculum.

Usage:
    python run_lesson.py               # Interactive menu
    python run_lesson.py --all         # Run all tests
    python run_lesson.py --progress    # Show progress
    python run_lesson.py --reset       # Reset progress and lesson files (prompts)
    python run_lesson.py --reset --yes # Reset without prompting
    python run_lesson.py 31            # Run a single lesson
"""

import json
import os
import re
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


def print_header(text, emoji="📚"):
    """Print a decorative header."""
    width = 60
    border = "=" * width
    print(f"\n{emoji} {text}")
    print(border)


def print_success(text):
    """Print a success message in green."""
    print(f"  ✅ {text}")


def print_error(text):
    """Print an error message in red."""
    print(f"  ❌ {text}")


def print_hint(text):
    """Print a hint message in yellow."""
    print(f"  💡 {text}")

def print_warning(text):
    """Print a warning message in yellow."""
    print(f"  ⚠️  {text}")

def print_badge(badge_info):
    """Print a badge award message."""
    print(f"\n  🎉 BADGE EARNED: {badge_info['emoji']} {badge_info['name']}")


def _check_lesson_compiles(lesson_num):
    """Return True if the lesson's source file compiles (or is absent)."""
    lesson_files = list(LESSONS_DIR.glob(f"{lesson_num:02d}_*.py"))
    if not lesson_files:
        return True
    lesson_path = lesson_files[0]
    try:
        with open(lesson_path, "r") as f:
            compile(f.read(), str(lesson_path), "exec")
    except SyntaxError as e:
        print_error(f"Lesson {lesson_num} has syntax error: {e}")
        return False
    return True


def run_lesson_tests(lesson_num):
    """Run tests for a specific lesson.

    Resolves the lesson's numbered test file and delegates to
    run_lesson_tests_from_file so any test_*.py is supported uniformly.
    """
    test_file = TESTS_DIR / f"test_{lesson_num:02d}.py"
    return run_lesson_tests_from_file(test_file, label=f"Lesson {lesson_num}")


def run_lesson_tests_from_file(test_file, label=None):
    """Run every test_* function in the given test module file.

    Each test file is loaded by path (so names like test_capstone_game.py
    work), executed, and its test_* functions are run with friendly output.
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

    # Import the test module
    import importlib.util
    spec = importlib.util.spec_from_file_location(stem, test_file)
    test_module = importlib.util.module_from_spec(spec)

    # Don't execute lesson code (it may have input() calls)
    # Just compile to check syntax (already done above)

    try:
        spec.loader.exec_module(test_module)
    except Exception as e:
        print_error(f"Failed to load test file: {e}")
        traceback.print_exc()
        return False

    # Find all test functions
    test_functions = [
        (name, func)
        for name, func in vars(test_module).items()
        if name.startswith("test_") and callable(func)
    ]

    if not test_functions:
        print_hint("No test functions found in test file.")
        return True

    passed = 0
    failed = 0
    total = len(test_functions)

    print(f"\n  Running {total} test(s)...\n")

    for test_name, test_func in test_functions:
        try:
            test_func()
            print_success(f"{test_name}")
            passed += 1
        except AssertionError as e:
            print_error(f"{test_name}: {e}")
            failed += 1
        except Exception as e:
            print_error(f"{test_name}: Unexpected error: {e}")
            failed += 1

    print(f"\n  Results: {passed}/{total} passed")

    if failed > 0:
        print_hint(f"{failed} test(s) failed. Check your code and try again!")
        return False
    else:
        print_success("All tests passed! 🎉")
        return True


def show_lesson(lesson_num):
    """Display the lesson instructions."""
    lesson_file = LESSONS_DIR / f"{lesson_num:02d}_*.py"
    lesson_files = list(LESSONS_DIR.glob(f"{lesson_num:02d}_*.py"))
    if not lesson_files:
        print_error(f"Lesson {lesson_num} not found!")
        return False

    lesson_path = lesson_files[0]
    with open(lesson_path, "r") as f:
        content = f.read()

    # Extract the docstring as instructions
    if content.startswith('"""'):
        end = content.find('"""', 3)
        if end != -1:
            instructions = content[3:end]
            print_header(f"Lesson {lesson_num}", "📚")
            print(instructions)
            print("=" * 60)
            return True

    print_header(f"Lesson {lesson_num}", "📚")
    print(content[:500])
    print("=" * 60)
    return True


def run_lesson(lesson_num):
    """Run a single lesson: show instructions, run tests, track progress."""
    if lesson_num < 1 or lesson_num > TOTAL_LESSONS:
        print_error(f"Lesson {lesson_num} not found. Lessons are 1-{TOTAL_LESSONS}.")
        return

    progress = load_progress()
    start_time = time.time()

    # Show lesson
    if not show_lesson(lesson_num):
        return

    # Run tests
    success = run_lesson_tests(lesson_num)

    elapsed = (time.time() - start_time) / 60
    progress["total_time_minutes"] += elapsed

    if success:
        if lesson_num not in progress["completed"]:
            progress["completed"].append(lesson_num)
            print_success(f"Lesson {lesson_num} completed! Added to your progress.")

        progress["current_lesson"] = lesson_num + 1

        # Check for new badges
        new_badges = check_badges(progress)
        for badge in new_badges:
            print_badge(badge)

        # Show next lesson suggestion
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
    badges = progress["badges"]
    badge_summary = ""
    if badges:
        badge_summary = f"\n\n  Badges ({len(badges)}):\n"
        for badge_key in badges:
            badge = BADGES.get(badge_key, {})
            badge_summary += f"    {badge.get('emoji', '🔹')} {badge.get('name', badge_key)}\n"
    else:
        badge_summary = "\n\n  No badges yet. Complete lessons to earn them!"
    completed_summary = ""
    if completed:
        completed_summary = f"\n\n  Completed lessons: {', '.join(str(l) for l in sorted(completed))}\n"
    next_lesson = progress["current_lesson"]
    next_summary = ""
    if next_lesson <= TOTAL_LESSONS:
        next_summary = f"\n  Next lesson: {next_lesson}\n  Run: python run_lesson.py {next_lesson}\n"
    summary = (
        f"\n  {label}: [{bar}] {completed_count}/{TOTAL_LESSONS}\n"
        f"  Time spent: {progress['total_time_minutes']:.1f} minutes\n"
        f"  Streak: {progress['streak_days']} days"
        f"{badge_summary}"
        f"{completed_summary}"
        f"{next_summary}"
    )
    print(summary)


def show_progress():
    """Display the student's progress."""
    progress = load_progress()
    print_header("Your Progress", "📊")
    render_progress_bar(progress, label="Progress")


def reset_progress(yes=False):
    """Reset progress and restore lesson files from scaffold templates.

    Guards: refuses to reset if any scaffold file fails to compile, so a
    corrupt template can never be copied into lessons/ and leave the
    student stuck.
    """
    import shutil

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

    if not yes:
        print_warning("This will reset all progress and lesson files.")
        confirm = input("Are you sure? (y/n): ").strip().lower()
        if confirm != "y":
            print("Reset cancelled.")
            return

    # Reset lesson files back to scaffold templates
    if SCAFFOLDS_DIR.exists():
        copied = 0
        for scaffold_file in SCAFFOLDS_DIR.glob("*.py"):
            dest = LESSONS_DIR / scaffold_file.name
            if dest.exists():
                dest.unlink()
            shutil.copy(scaffold_file, dest)
            copied += 1
        if copied:
            print_success(f"Restored {copied} lesson files from scaffolds/.")
    else:
        print_warning("No scaffold files found.")

    # Reset progress state
    if PROGRESS_FILE.exists():
        PROGRESS_FILE.unlink()
    initial_progress = {
        "current_lesson": 1,
        "completed": [],
        "badges": [],
        "total_time_minutes": 0,
        "streak_days": 0,
    }
    save_progress(initial_progress)
    print_header("Full Reset Complete!", "🔄")
    print_success("Progress cleared.")
    print_success("All lesson files reset to starter templates.")
    print("Starting fresh from lesson 1!")

def run_all_tests():
    """Run all lesson tests. Returns True if every suite passed."""
    print_header("Running All Tests", "🧪")

    all_passed = True

    # Discover every test_*.py so new suites (e.g. test_capstone_game) run too.
    test_files = sorted(TESTS_DIR.glob("test_*.py"))
    for test_file in test_files:
        if not test_file.exists():
            continue

        print(f"\n  {test_file.stem}:")
        success = run_lesson_tests_from_file(test_file)
        if not success:
            all_passed = False

    if all_passed:
        print_success("\nAll tests passed! 🎉")
    else:
        print_error("\nSome tests failed. Review the output above.")
    return all_passed


def interactive_loop():
    """Interactive menu: no args needed. Auto-opens current lesson, then shows navigation."""
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
            print(f"  Time: {progress['total_time_minutes']:.1f} min | Streak: {progress['streak_days']} days")

            badges = progress["badges"]
            if badges:
                print(f"\n  Badges ({len(badges)}):")
                for badge_key in badges:
                    badge = BADGES.get(badge_key, {})
                    print(f"    {badge.get('emoji', '🔹')} {badge.get('name', badge_key)}")

            print(f"\n  Current lesson: {current}")
            run_lesson(current)
            input("Press Enter to continue...")
            continue

        # All lessons done or current is completed — show menu
        if current > TOTAL_LESSONS:
            print_header("Python Adventure Curriculum", "🏆")
            print_success("All lessons completed! You are a Python Hero!")
            print_badge(BADGES["adventure_complete"])
        else:
            print_header("Python Adventure Curriculum", "🎮")
            render_progress_bar(progress, label="Progress")

            print("\n  Menu:")
        completed_rev = sorted(completed, reverse=True)[:8]
        if completed_rev:
            print(f"    {Color.CYAN}  p <num>{Color.RESET} - Open completed lesson: {', '.join(str(x) for x in completed_rev)}")
        if current <= TOTAL_LESSONS:
            print(f"    {Color.GREEN}  n{Color.RESET} - Retry current lesson ({current})")
        print(f"    {Color.BLUE}  i <num>{Color.RESET} - Preview any lesson")
        print(f"    {Color.YELLOW}  r{Color.RESET} - Reset everything")
        print(f"    {Color.MAGENTA}  q{Color.RESET} - Quit")

        try:
            choice = input("\nEnter choice: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if choice == "q":
            print("Goodbye!")
            break

        if choice == "n" and current <= TOTAL_LESSONS:
            run_lesson(current)
            input("Press Enter to continue...")
            continue

        if choice == "r":
            reset_progress()
            input("Press Enter to continue...")
            continue

        if choice.startswith("p ") and completed_rev:
            try:
                num = int(choice[2:].strip())
            except ValueError:
                print_error("Enter a valid lesson number.")
                input("Press Enter to continue...")
                continue
            run_lesson(num)
            input("Press Enter to continue...")
            continue

        if choice.startswith("i "):
            try:
                num = int(choice[2:].strip())
            except ValueError:
                print_error("Enter a valid lesson number.")
                input("Press Enter to continue...")
                continue
            show_lesson(num)
            print_hint("This is lesson preview.")
            input("Press Enter to continue...")
            continue

        print_error("Invalid option. Use n / p <num> / i <num> / r / q.")
        input("Press Enter to continue...")


def main():
    """Main entry point."""
    # Tests and lessons reference paths relative to this script, so make the
    # repo root the working directory regardless of where it is invoked from.
    os.chdir(BASE_DIR)

    if len(sys.argv) < 2:
        interactive_loop()
        return

    args = sys.argv[1:]
    force = "--yes" in args or "--force" in args

    if "--all" in args:
        ok = run_all_tests()
        sys.exit(0 if ok else 1)
    elif "--progress" in args:
        show_progress()
    elif "--reset" in args:
        reset_progress(yes=force)
    elif "--help" in args or "-h" in args:
        print(__doc__)
    else:
        # Remaining token is a lesson number.
        token = next((a for a in args if not a.startswith("--")), None)
        if token is None:
            print_error("Invalid arguments. Run with --help for usage.")
            return
        try:
            lesson_num = int(token)
            run_lesson(lesson_num)
        except ValueError:
            print_error(f"Invalid argument: {token}")
            print("Usage: python run_lesson.py <lesson_number>")


if __name__ == "__main__":
    main()
