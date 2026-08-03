"""Meta-tests: guard the quality of the lesson test suite itself.

These do not grade a student. They fail when the *curriculum* regresses:

* ``test_no_lesson_passes_on_a_blank_starter`` — the keystone. It copies every
  scaffold over a temporary lessons/ tree and runs each lesson's test module.
  A lesson whose tests all pass with no student code is a false completion,
  which is exactly the bug this suite was rebuilt to kill.
* every lesson has a scaffold, a test module and a guard against answer leaks.

Runs on the standard library only, so ``run_lesson.py`` can execute it too.
"""
import importlib.util
import io
import shutil
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).parent.parent
LESSONS_DIR = ROOT / "lessons"
SCAFFOLDS_DIR = ROOT / "scaffolds"
TESTS_DIR = ROOT / "tests"
TOTAL_LESSONS = 50

LESSON_NUMBERS = list(range(1, TOTAL_LESSONS + 1))


def _lesson_file(num, directory):
    matches = sorted(directory.glob(f"{num:02d}_*.py"))
    return matches[0] if matches else None


def test_every_lesson_has_a_scaffold():
    missing = [n for n in LESSON_NUMBERS if _lesson_file(n, SCAFFOLDS_DIR) is None]
    assert not missing, f"Lessons without a scaffold: {missing}"


def test_every_lesson_has_a_test_module():
    missing = [
        n for n in LESSON_NUMBERS if not (TESTS_DIR / f"test_{n:02d}.py").exists()
    ]
    assert not missing, f"Lessons without a test module: {missing}"


def test_every_test_module_guards_the_scaffold():
    missing = [
        n
        for n in LESSON_NUMBERS
        if "assert_scaffold_is_blank" not in (TESTS_DIR / f"test_{n:02d}.py").read_text()
    ]
    assert not missing, (
        f"These lesson tests don't check that the shipped scaffold is blank: "
        f"{missing}"
    )


def test_no_test_asserts_against_the_instruction_docstring():
    """Reading the raw lesson text lets the instructions fake a pass.

    Tests must go through ``student_code``/``run_student`` (docstring
    stripped) instead of ``read_text()`` on the lesson file.
    """
    offenders = []
    for n in LESSON_NUMBERS:
        src = (TESTS_DIR / f"test_{n:02d}.py").read_text()
        if "lesson_text(" in src or 'glob("' in src and "read_text()" in src:
            offenders.append(n)
    assert not offenders, (
        f"These tests read the raw lesson file (docstring included), so the "
        f"instructions can satisfy them: {offenders}"
    )


def _run_module_against_blank_lessons(num, sandbox):
    """Run one lesson's test module inside a sandbox with blank lessons.

    Returns (passed, total).
    """
    test_file = sandbox / "tests" / f"test_{num:02d}.py"
    spec = importlib.util.spec_from_file_location(f"blankcheck_{num:02d}", test_file)
    if spec is None or spec.loader is None:
        return 0, 1
    module = importlib.util.module_from_spec(spec)
    try:
        with redirect_stdout(io.StringIO()):
            spec.loader.exec_module(module)
    except Exception:
        return 0, 1  # a module that won't even import certainly doesn't pass
    funcs = [
        (name, fn)
        for name, fn in list(vars(module).items())
        if name.startswith("test_") and callable(fn)
    ]
    # Reference tests exercise answer_key/ on purpose; they are teacher-side
    # documentation, not student grading, so they legitimately pass.
    graded = [(n, f) for n, f in funcs if not n.startswith("test_reference")]
    passed = 0
    for _name, fn in graded:
        try:
            with redirect_stdout(io.StringIO()):
                fn()
            passed += 1
        except BaseException:
            # Covers both failures and pytest.skip (an unattempted lesson),
            # neither of which is a pass.
            pass
    return passed, len(graded)


def test_no_lesson_passes_on_a_blank_starter():
    """The keystone guard: an untouched starter file must never pass."""
    sandbox = Path(tempfile.mkdtemp(prefix="blankcheck_"))
    try:
        for name in ("tests", "answer_key", "scaffolds"):
            src = ROOT / name
            if src.exists():
                shutil.copytree(src, sandbox / name, ignore=shutil.ignore_patterns("__pycache__"))
        (sandbox / "lessons").mkdir()
        for scaffold in SCAFFOLDS_DIR.glob("*.py"):
            shutil.copy(scaffold, sandbox / "lessons" / scaffold.name)
        shutil.copy(ROOT / "main.py", sandbox / "main.py")

        # Point the helpers at the sandbox by importing a fresh copy.
        saved_path = list(sys.path)
        saved_helpers = sys.modules.pop("_helpers", None)
        sys.path.insert(0, str(sandbox / "tests"))
        try:
            free_passes = {}
            for n in LESSON_NUMBERS:
                for mod in [m for m in sys.modules if m.startswith("blankcheck_")]:
                    del sys.modules[mod]
                sys.modules.pop("_helpers", None)
                passed, total = _run_module_against_blank_lessons(n, sandbox)
                if total and passed == total:
                    free_passes[n] = f"{passed}/{total}"
        finally:
            sys.path[:] = saved_path
            sys.modules.pop("_helpers", None)
            if saved_helpers is not None:
                sys.modules["_helpers"] = saved_helpers
    finally:
        shutil.rmtree(sandbox, ignore_errors=True)

    assert not free_passes, (
        "These lessons pass their whole test suite with NO student code "
        f"(false completions): {free_passes}"
    )
