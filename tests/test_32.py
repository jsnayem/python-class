"""Tests for Lesson 32: Hero Stats"""
from pathlib import Path


def test_file_exists():
    lesson_files = sorted(Path("lessons").glob("32_*.py"))
    assert lesson_files, "Lesson 32 file should exist"


def test_has_is_alive():
    text = (Path("lessons") / next(Path("lessons").glob("32_*.py")).name).read_text()
    assert "is_alive" in text


def test_is_valid_python():
    text = (Path("lessons") / next(Path("lessons").glob("32_*.py")).name).read_text()
    try:
        compile(text, "lessons/32_hero_stats.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
