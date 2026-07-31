"""Tests for Lesson 18: Tuples"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("18_*.py"))
    assert lesson_files, "Lesson 18 file should exist"


def test_has_tuple():
    text = (Path("lessons") / next(Path("lessons").glob("18_*.py")).name).read_text()
    assert "(" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("18_*.py")).name).read_text()
    try:
        compile(text, "lessons/18_tuples.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
