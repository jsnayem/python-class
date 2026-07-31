"""Tests for Lesson 26: File Reading"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("26_*.py"))
    assert lesson_files, "Lesson 26 file should exist"


def test_opens_file():
    text = (Path("lessons") / next(Path("lessons").glob("26_*.py")).name).read_text()
    assert "open(" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("26_*.py")).name).read_text()
    try:
        compile(text, "lessons/26_file_reading.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
