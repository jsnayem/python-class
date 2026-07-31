"""Tests for Lesson 44: Save System"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("44_*.py"))
    assert lesson_files, "Lesson 44 file should exist"


def test_saves_json():
    text = (Path("lessons") / next(Path("lessons").glob("44_*.py")).name).read_text()
    assert "json" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("44_*.py")).name).read_text()
    try:
        compile(text, "lessons/44_save_system.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
