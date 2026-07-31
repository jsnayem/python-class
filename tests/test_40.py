"""Tests for Lesson 40: Flee Mechanic"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("40_*.py"))
    assert lesson_files, "Lesson 40 file should exist"


def test_has_flee():
    text = (Path("lessons") / next(Path("lessons").glob("40_*.py")).name).read_text()
    assert "flee" in text.lower()


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("40_*.py")).name).read_text()
    try:
        compile(text, "lessons/40_flee_mechanic.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
