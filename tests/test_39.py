"""Tests for Lesson 39: Attack Logic"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("39_*.py"))
    assert lesson_files, "Lesson 39 file should exist"


def test_has_function():
    text = (Path("lessons") / next(Path("lessons").glob("39_*.py")).name).read_text()
    assert "def " in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("39_*.py")).name).read_text()
    try:
        compile(text, "lessons/39_attack_logic.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
