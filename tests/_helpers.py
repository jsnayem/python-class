"""Shared test helpers for the lesson test suite.

Design rules for every lesson test (see tests/README.md):

1. NEVER assert on text that lives in the lesson's instruction docstring.
   Always read the student's own code via ``student_code(n)`` — the docstring
   is stripped, so "the word 'class' appears in the instructions" can no
   longer fake a pass.
2. PREFER behaviour over spelling. Execute the student's file with
   ``run_student(n)`` and assert on the resulting values/output instead of
   requiring an exact source substring like ``hero_gold + 20`` (which
   forbids the equally correct ``hero_gold += 20``).
3. Every lesson test module must call ``requires_student_code(n)`` (directly
   or via ``run_student``) so a blank starter file can never pass. An
   unattempted lesson *skips*, so a student sees red only for work they have
   actually attempted.
4. Use ``ROOT``-anchored paths so tests run from any working directory.
"""
import ast
import importlib.util
import io
import os
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).parent.parent
LESSONS_DIR = ROOT / "lessons"
SCAFFOLDS_DIR = ROOT / "scaffolds"

TODO_MARKER = "TODO: Write your code for Lesson"


class _EmptyInput:
    """A stdin stand-in that always yields an empty line for input().

    ``input()`` calls ``readline()``; returning "\\n" (not "") makes every
    prompt return an empty string without blocking or raising EOFError, no
    matter how many times the student's code calls input().
    """

    def readline(self, size: int = -1) -> str:
        return "\n"

    def read(self, size: int = -1) -> str:
        return ""

    def readlines(self):
        return []

    def close(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        return ""


def load_module(modname: str, rel_path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(modname, rel_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {rel_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_answer(modname: str) -> Any:
    """Load a teacher reference solution from answer_key/.

    Reference tests document the intended behaviour; they do NOT grade the
    student. Name such tests ``test_reference_*`` so nobody mistakes them
    for student grading.
    """
    return load_module(modname, ROOT / "answer_key" / f"{modname}.py")


def lesson_path(num: int) -> Path:
    matches = sorted(LESSONS_DIR.glob(f"{num:02d}_*.py"))
    assert matches, f"Lesson {num} file should exist in lessons/"
    return matches[0]


def scaffold_path(num: int) -> Path:
    matches = sorted(SCAFFOLDS_DIR.glob(f"{num:02d}_*.py"))
    assert matches, f"Scaffold for lesson {num} should exist in scaffolds/"
    return matches[0]


def lesson_text(num: int) -> str:
    return lesson_path(num).read_text()


def docstring_bounds(source: str):
    """Locate the leading module docstring, allowing a string prefix.

    Lessons that teach escape sequences use a raw docstring (r\"\"\"...\"\"\") so
    that \\n and \\t show up literally in the instructions instead of being
    turned into a real newline or tab. Returns (start, end) indexes of the
    opening and closing triple quotes, or None when there is no docstring.
    """
    stripped = source.lstrip()
    offset = len(source) - len(stripped)
    prefix = 0
    while prefix < 2 and prefix < len(stripped) and stripped[prefix] in "rRbBuUfF":
        prefix += 1
    for quote in ('"""', "'''"):
        if stripped[prefix:].startswith(quote):
            start = offset + prefix
            end = source.find(quote, start + 3)
            if end == -1:
                return None
            return start, end + 3
    return None


def strip_docstring(source: str) -> str:
    """Return source with its leading module docstring removed.

    Only a docstring at the very top of the file is stripped, so a student's
    own triple-quoted comments later in the file are left intact.
    """
    bounds = docstring_bounds(source)
    if bounds is None:
        return source
    return source[bounds[1]:]


def student_code(lesson_num: int) -> str:
    """The student's own code for a lesson (instruction docstring removed)."""
    return strip_docstring(lesson_text(lesson_num))


def _meaningful_lines(code: str) -> list:
    return [
        line
        for line in code.splitlines()
        if line.strip() and TODO_MARKER not in line and not line.strip().startswith("#")
    ]


def is_blank_scaffold(lesson_num: int) -> bool:
    """True when the lesson file still holds no student code at all."""
    return not _meaningful_lines(student_code(lesson_num))


def requires_student_code(lesson_num: int) -> str:
    """Skip until the student writes code; then return that code.

    An unattempted lesson is *pending*, not broken, so it skips rather than
    fails: a student who has finished lesson 7 should see a clean run, not 43
    red lessons they haven't reached. The blank-starter guard still holds,
    because a skip never counts as a pass.
    """
    code = student_code(lesson_num)
    if not _meaningful_lines(code):
        pytest.skip(
            f"Lesson {lesson_num} not started yet — open "
            f"{lesson_path(lesson_num).name} and write your solution below "
            f"the TODO line."
        )
    return code


def compiles(lesson_num: int) -> None:
    """Fail with a friendly message if the lesson has a syntax error."""
    path = lesson_path(lesson_num)
    try:
        compile(path.read_text(), str(path), "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax in {path.name}: {e}")


class safe_stdin:
    """Context manager that keeps a lesson's input() from blocking the suite.

    Some lesson files call input() at import time. When a behavioral test
    exec's such a file, stdin is replaced with an empty stream (so input()
    returns "") and a wall-clock alarm guards against accidental infinite
    loops. Restores the original stdin on exit.
    """

    def __init__(self, timeout: float = 5.0):
        self.timeout = timeout
        self._old_stdin = None
        self._old_handler = None

    def __enter__(self):
        import signal

        self._old_stdin = sys.stdin
        sys.stdin = _EmptyInput()  # input() -> "" instead of blocking
        if hasattr(signal, "SIGALRM"):
            def _handler(signum, frame):  # pragma: no cover - real runs only
                raise TimeoutError(
                    f"Lesson code ran longer than {self.timeout}s (possible infinite loop)"
                )
            self._old_handler = signal.signal(signal.SIGALRM, _handler)
            signal.alarm(int(self.timeout))
        return self

    def __exit__(self, exc_type, exc, tb):
        import signal

        if self._old_handler is not None:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, self._old_handler)
        if self._old_stdin is not None:
            sys.stdin = self._old_stdin
        return False


class StudentRun:
    """Result of executing a student's lesson file."""

    def __init__(self, namespace: dict, output: str):
        self.ns = namespace
        self.output = output

    def get(self, name, default=None):
        return self.ns.get(name, default)

    def __contains__(self, name):
        return name in self.ns


def run_student(lesson_num: int, isolate_files: bool = True) -> StudentRun:
    """Execute the student's lesson file and capture namespace + stdout.

    Guards first that real student code exists. Runs with a stubbed stdin and
    a timeout, and (by default) inside a throwaway working directory so
    lessons that write files never litter or read stale repo artifacts.
    """
    requires_student_code(lesson_num)
    compiles(lesson_num)
    path = lesson_path(lesson_num)
    source = path.read_text()
    ns: dict = {"__name__": "__main__", "__file__": str(path)}
    buf = io.StringIO()
    old_cwd = os.getcwd()
    tmp = tempfile.mkdtemp(prefix=f"lesson{lesson_num:02d}_") if isolate_files else None
    try:
        if tmp:
            os.chdir(tmp)
        with safe_stdin(), redirect_stdout(buf):
            exec(compile(source, str(path), "exec"), ns)
    except AssertionError:
        raise
    except Exception as e:
        raise AssertionError(
            f"Running {path.name} raised {type(e).__name__}: {e}"
        ) from e
    finally:
        os.chdir(old_cwd)
    return StudentRun(ns, buf.getvalue())


def student_tree(lesson_num: int) -> ast.AST:
    """Parse the student's code (docstring stripped) into an AST."""
    return ast.parse(requires_student_code(lesson_num))


def defines_function(lesson_num: int, name: str) -> bool:
    return any(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == name
        for n in ast.walk(student_tree(lesson_num))
    )


def defines_class(lesson_num: int, name: str) -> bool:
    return any(
        isinstance(n, ast.ClassDef) and n.name == name
        for n in ast.walk(student_tree(lesson_num))
    )


def uses_node(lesson_num: int, node_types: tuple) -> bool:
    """True when the student's code contains any of the given AST node types."""
    return any(isinstance(n, node_types) for n in ast.walk(student_tree(lesson_num)))


def count_calls(lesson_num: int, func_name: str) -> int:
    """How many times the student calls a given function by name."""
    total = 0
    for n in ast.walk(student_tree(lesson_num)):
        if isinstance(n, ast.Call):
            f = n.func
            if isinstance(f, ast.Name) and f.id == func_name:
                total += 1
            elif isinstance(f, ast.Attribute) and f.attr == func_name:
                total += 1
    return total


def assert_scaffold_is_blank(lesson_num: int) -> None:
    """The shipped starter template must never contain the answer."""
    text = scaffold_path(lesson_num).read_text()
    assert TODO_MARKER in text, (
        f"scaffolds/{scaffold_path(lesson_num).name} must be a blank starter "
        f"template containing the '{TODO_MARKER}' marker."
    )
    assert not _meaningful_lines(strip_docstring(text)), (
        f"scaffolds/{scaffold_path(lesson_num).name} leaks answer code — a "
        f"starter template must contain only instructions and the TODO line."
    )
