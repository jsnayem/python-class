"""Tests for Lesson 13: For Loops"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("13_*.py"))
    assert lesson_files, "Lesson 13 file should exist"


def test_has_for_loop():
    text = (Path("lessons") / next(Path("lessons").glob("13_*.py")).name).read_text()
    assert "for " in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("13_*.py")).name).read_text()
    try:
        compile(text, "lessons/13_for_loops.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
