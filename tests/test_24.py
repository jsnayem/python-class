"""Tests for Lesson 24: Error Handling"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("24_*.py"))
    assert lesson_files, "Lesson 24 file should exist"


def test_has_try_except():
    text = (Path("lessons") / next(Path("lessons").glob("24_*.py")).name).read_text()
    assert "try" in text
    assert "except" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("24_*.py")).name).read_text()
    try:
        compile(text, "lessons/24_try_except.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
