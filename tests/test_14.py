"""Tests for Lesson 14: Functions Intro"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("14_*.py"))
    assert lesson_files, "Lesson 14 file should exist"


def test_has_function():
    text = (Path("lessons") / next(Path("lessons").glob("14_*.py")).name).read_text()
    assert "def " in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("14_*.py")).name).read_text()
    try:
        compile(text, "lessons/14_functions_intro.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
