"""Tests for Lesson 41: Shop System"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("41_*.py"))
    assert lesson_files, "Lesson 41 file should exist"


def test_has_shop():
    text = (Path("lessons") / next(Path("lessons").glob("41_*.py")).name).read_text()
    assert "shop" in text.lower()


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("41_*.py")).name).read_text()
    try:
        compile(text, "lessons/41_shop_system.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
