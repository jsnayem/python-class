"""Tests for Lesson 23: Inheritance - Shop Items"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("23_*.py"))
    assert lesson_files, "Lesson 23 file should exist"


def test_has_multiple_classes():
    text = (Path("lessons") / next(Path("lessons").glob("23_*.py")).name).read_text()
    assert text.count("class ") >= 2


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("23_*.py")).name).read_text()
    try:
        compile(text, "lessons/23_inheritance.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
