"""Tests for Lesson 17: Classes Introduction"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("17_*.py"))
    assert lesson_files, "Lesson 17 file should exist"


def test_has_class():
    text = (Path("lessons") / next(Path("lessons").glob("17_*.py")).name).read_text()
    assert "class " in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("17_*.py")).name).read_text()
    try:
        compile(text, "lessons/17_dictionaries.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
