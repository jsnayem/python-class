"""Tests for Lesson 40: Flee Mechanic."""
from pathlib import Path

from _helpers import load_answer, lesson_text

ROOT = Path(__file__).parent.parent


def test_student_file_present():
    assert list((ROOT / "lessons").glob("40_*.py")), "Lesson 40 file should exist"


def test_student_has_flee_function():
    assert "def flee" in lesson_text(40)


def test_answer_flee_bounds():
    m = load_answer("40_flee_mechanic")
    assert m.flee(chance=1.0) is True
    assert m.flee(chance=0.0) is False
    for _ in range(50):
        assert m.flee() in (True, False)
