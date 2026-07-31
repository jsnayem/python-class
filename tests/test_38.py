"""Tests for Lesson 38: Combat System"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("38_*.py"))
    assert lesson_files, "Lesson 38 file should exist"


def test_has_function():
    text = (Path("lessons") / next(Path("lessons").glob("38_*.py")).name).read_text()
    assert "def " in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("38_*.py")).name).read_text()
    try:
        compile(text, "lessons/38_combat_system.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
