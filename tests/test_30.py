"""Tests for Lesson 30: F-Strings"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("30_*.py"))
    assert lesson_files, "Lesson 30 file should exist"


def test_uses_f_string():
    text = (Path("lessons") / next(Path("lessons").glob("30_*.py")).name).read_text()
    assert 'f"' in text or "f'" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("30_*.py")).name).read_text()
    try:
        compile(text, "lessons/30_f_strings.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
