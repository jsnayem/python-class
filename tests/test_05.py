"""Tests for Lesson 5: Strings"""
import io
from contextlib import redirect_stdout


def test_strings_created():
    with open("lessons/05_strings.py", "r") as f:
        content = f.read()
    assert "monster_name" in content
    assert "monster_desc" in content


def test_uppercase_lowercase():
    with open("lessons/05_strings.py", "r") as f:
        content = f.read()
    assert "upper()" in content
    assert "lower()" in content


def test_string_combination():
    with open("lessons/05_strings.py", "r") as f:
        content = f.read()
    assert 'f"' in content or "f'" in content
    assert "print(" in content


def test_is_valid_python():
    with open("lessons/05_strings.py", "r") as f:
        content = f.read()
    try:
        compile(content, "lessons/05_strings.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
