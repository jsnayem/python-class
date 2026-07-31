"""Tests for Lesson 28: Randomness"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("28_*.py"))
    assert lesson_files, "Lesson 28 file should exist"


def test_uses_random():
    text = (Path("lessons") / next(Path("lessons").glob("28_*.py")).name).read_text()
    assert "random" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("28_*.py")).name).read_text()
    try:
        compile(text, "lessons/28_random.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
