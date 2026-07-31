"""Tests for Lesson 48: Objectives"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("48_*.py"))
    assert lesson_files, "Lesson 48 file should exist"


def test_has_objectives():
    text = (Path("lessons") / next(Path("lessons").glob("48_*.py")).name).read_text()
    assert "objective" in text.lower()


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("48_*.py")).name).read_text()
    try:
        compile(text, "lessons/48_objectives.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
