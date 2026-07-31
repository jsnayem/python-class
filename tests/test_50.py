"""Tests for Lesson 50: Play and Share"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("50_*.py"))
    assert lesson_files, "Lesson 50 file should exist"


def test_has_credits():
    text = (Path("lessons") / next(Path("lessons").glob("50_*.py")).name).read_text()
    assert "credit" in text.lower() or "congratulations" in text.lower()


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("50_*.py")).name).read_text()
    try:
        compile(text, "lessons/50_play_and_share.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
