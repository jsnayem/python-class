"""Tests for Lesson 37: Monster Class"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("37_*.py"))
    assert lesson_files, "Lesson 37 file should exist"


def test_has_monster_class():
    text = (Path("lessons") / next(Path("lessons").glob("37_*.py")).name).read_text()
    assert "class " in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("37_*.py")).name).read_text()
    try:
        compile(text, "lessons/37_monster_class.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
