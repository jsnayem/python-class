"""Tests for Lesson 16: Return Values"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("16_*.py"))
    assert lesson_files, "Lesson 16 file should exist"


def test_has_return():
    text = (Path("lessons") / next(Path("lessons").glob("16_*.py")).name).read_text()
    assert "return " in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("16_*.py")).name).read_text()
    try:
        compile(text, "lessons/16_return_values.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
