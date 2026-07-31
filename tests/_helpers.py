"""Shared test helpers.

Loads a module (lesson student file or answer_key/ reference) from a path
without polluting sys.modules. Resolves the Pyright "ModuleSpec | None"
complaint by guaranteeing a non-None spec from a known-existing file.
"""
import importlib.util
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).parent.parent


class _EmptyInput:
    """A stdin stand-in that always yields an empty line for input().

    ``input()`` calls ``readline()``; returning \"\" (not raising EOF) makes
    every prompt return an empty string without blocking or erroring, no
    matter how many times the student's code calls input().
    """

    def readline(self, size: int = -1) -> str:
        # Return a newline (not "") so input() yields "" without raising
        # EOFError; returning it every call supports multiple input() prompts.
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
    return load_module(modname, ROOT / "answer_key" / f"{modname}.py")


def lesson_text(num: int) -> str:
    path = ROOT / "lessons" / next((ROOT / "lessons").glob(f"{num:02d}_*.py"))
    return path.read_text()


def strip_docstring(source: str) -> str:
    """Return source with its leading module docstring removed.

    Only a docstring at the very top of the file (the first non-blank token
    is a triple-quoted string) is stripped, so a student's own triple-quoted
    comments later in the file are left intact.
    """
    stripped = source.lstrip()
    if not stripped.startswith('"""'):
        return source
    end = source.find('"""', 3)
    if end == -1:
        return source
    return source[end + 3:]


def student_code(lesson_num: int) -> str:
    """Read a lesson file and return only the student's code (docstring stripped)."""
    return strip_docstring(lesson_text(lesson_num))


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
        import io
        import signal

        self._old_stdin = sys.stdin
        # An endless empty source so every input() returns "" without ever
        # blocking or raising EOFError, regardless of how many calls the
        # student's code makes.
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
