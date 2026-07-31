"""Tests for Lesson 29: Time"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("29_*.py"))
    assert lesson_files, "Lesson 29 file should exist"


def test_uses_time():
    text = (Path("lessons") / next(Path("lessons").glob("29_*.py")).name).read_text()
    assert "time" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("29_*.py")).name).read_text()
    try:
        compile(text, "lessons/29_time.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
