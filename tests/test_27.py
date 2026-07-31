"""Tests for Lesson 27: JSON"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("27_*.py"))
    assert lesson_files, "Lesson 27 file should exist"


def test_uses_json():
    text = (Path("lessons") / next(Path("lessons").glob("27_*.py")).name).read_text()
    assert "json" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("27_*.py")).name).read_text()
    try:
        compile(text, "lessons/27_json.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
