"""Tests for Lesson 46: Color System"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("46_*.py"))
    assert lesson_files, "Lesson 46 file should exist"


def test_has_color():
    text = (Path("lessons") / next(Path("lessons").glob("46_*.py")).name).read_text()
    assert "color" in text.lower()


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("46_*.py")).name).read_text()
    try:
        compile(text, "lessons/46_color_system.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
