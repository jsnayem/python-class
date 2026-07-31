"""Tests for Lesson 31: Hero Class"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("31_*.py"))
    assert lesson_files, "Lesson 31 file should exist"


def test_has_hero_class():
    text = (Path("lessons") / next(Path("lessons").glob("31_*.py")).name).read_text()
    assert "class Hero" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("31_*.py")).name).read_text()
    try:
        compile(text, "lessons/31_hero_class.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
