"""Tests for Lesson 34: Item Class"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("34_*.py"))
    assert lesson_files, "Lesson 34 file should exist"


def test_has_item_class():
    text = (Path("lessons") / next(Path("lessons").glob("34_*.py")).name).read_text()
    assert "class Item" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("34_*.py")).name).read_text()
    try:
        compile(text, "lessons/34_item_class.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
