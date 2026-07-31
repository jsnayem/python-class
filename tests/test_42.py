"""Tests for Lesson 42: World Map"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("42_*.py"))
    assert lesson_files, "Lesson 42 file should exist"


def test_has_world():
    text = (Path("lessons") / next(Path("lessons").glob("42_*.py")).name).read_text()
    assert "world" in text.lower()


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("42_*.py")).name).read_text()
    try:
        compile(text, "lessons/42_world_map.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
