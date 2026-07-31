"""Tests for Lesson 45: Load System"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("45_*.py"))
    assert lesson_files, "Lesson 45 file should exist"


def test_loads_json():
    text = (Path("lessons") / next(Path("lessons").glob("45_*.py")).name).read_text()
    assert "json" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("45_*.py")).name).read_text()
    try:
        compile(text, "lessons/45_load_system.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
