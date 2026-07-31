"""Tests for Lesson 19: Classes Introduction"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("19_*.py"))
    assert lesson_files, "Lesson 19 file should exist"


def test_has_multiple_classes():
    text = (Path("lessons") / next(Path("lessons").glob("19_*.py")).name).read_text()
    assert text.count("class ") >= 2


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("19_*.py")).name).read_text()
    try:
        compile(text, "lessons/19_classes_intro.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
