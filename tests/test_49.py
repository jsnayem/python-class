"""Tests for Lesson 49: Final Integration"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("49_*.py"))
    assert lesson_files, "Lesson 49 file should exist"


def test_has_header():
    text = (Path("lessons") / next(Path("lessons").glob("49_*.py")).name).read_text()
    assert "header" in text.lower() or "GAME START" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("49_*.py")).name).read_text()
    try:
        compile(text, "lessons/49_final_integration.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
