"""Tests for Lesson 11: Functions - Making a Spell"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("11_*.py"))
    assert lesson_files, "Lesson 11 file should exist"


def test_has_function():
    text = (Path("lessons") / next(Path("lessons").glob("11_*.py")).name).read_text()
    assert "def " in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("11_*.py")).name).read_text()
    try:
        compile(text, "lessons/11_loops_intro.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
