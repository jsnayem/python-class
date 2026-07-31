"""Tests for Lesson 15: Dictionary Methods"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("15_*.py"))
    assert lesson_files, "Lesson 15 file should exist"


def test_uses_dict():
    text = (Path("lessons") / next(Path("lessons").glob("15_*.py")).name).read_text()
    assert "{" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("15_*.py")).name).read_text()
    try:
        compile(text, "lessons/15_function_args.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
