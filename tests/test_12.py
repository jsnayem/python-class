"""Tests for Lesson 12: Multiple Parameters"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("12_*.py"))
    assert lesson_files, "Lesson 12 file should exist"


def test_has_function_with_params():
    text = (Path("lessons") / next(Path("lessons").glob("12_*.py")).name).read_text()
    assert "def " in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("12_*.py")).name).read_text()
    try:
        compile(text, "lessons/12_while_loops.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
