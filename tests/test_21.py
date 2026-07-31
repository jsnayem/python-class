"""Tests for Lesson 21: Class Attributes"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("21_*.py"))
    assert lesson_files, "Lesson 21 file should exist"


def test_has_class_attribute():
    text = (Path("lessons") / next(Path("lessons").glob("21_*.py")).name).read_text()
    assert "class " in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("21_*.py")).name).read_text()
    try:
        compile(text, "lessons/21_attributes.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
