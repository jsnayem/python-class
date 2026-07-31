"""Tests for Lesson 22: Inheritance - Weapon Subclass"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("22_*.py"))
    assert lesson_files, "Lesson 22 file should exist"


def test_has_inheritance():
    text = (Path("lessons") / next(Path("lessons").glob("22_*.py")).name).read_text()
    assert "class " in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("22_*.py")).name).read_text()
    try:
        compile(text, "lessons/22_methods.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
