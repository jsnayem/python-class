"""Tests for Lesson 43: Game Loop"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("43_*.py"))
    assert lesson_files, "Lesson 43 file should exist"


def test_has_loop():
    text = (Path("lessons") / next(Path("lessons").glob("43_*.py")).name).read_text()
    assert "while " in text or "for " in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("43_*.py")).name).read_text()
    try:
        compile(text, "lessons/43_game_loop.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
