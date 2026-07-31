"""Tests for Lesson 33: Hero Inventory"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("33_*.py"))
    assert lesson_files, "Lesson 33 file should exist"


def test_has_inventory():
    text = (Path("lessons") / next(Path("lessons").glob("33_*.py")).name).read_text()
    assert "inventory" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("33_*.py")).name).read_text()
    try:
        compile(text, "lessons/33_hero_inventory.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
