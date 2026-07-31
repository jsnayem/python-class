"""Tests for Lesson 25: File Writing"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("25_*.py"))
    assert lesson_files, "Lesson 25 file should exist"


def test_opens_file():
    text = (Path("lessons") / next(Path("lessons").glob("25_*.py")).name).read_text()
    assert "open(" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("25_*.py")).name).read_text()
    try:
        compile(text, "lessons/25_file_writing.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
