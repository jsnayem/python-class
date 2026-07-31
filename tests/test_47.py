"""Tests for Lesson 47: Decorative UI"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("47_*.py"))
    assert lesson_files, "Lesson 47 file should exist"


def test_has_print():
    text = (Path("lessons") / next(Path("lessons").glob("47_*.py")).name).read_text()
    assert "print(" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("47_*.py")).name).read_text()
    try:
        compile(text, "lessons/47_decorative_ui.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
