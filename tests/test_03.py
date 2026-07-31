"""Tests for Lesson 3: Printing with Style"""
import io
from contextlib import redirect_stdout

from _helpers import safe_stdin


def test_has_title_border():
    f = io.StringIO()
    with safe_stdin(), redirect_stdout(f):
        exec(open("lessons/03_printing.py").read())
    output = f.getvalue()
    assert "=" in output


def test_prints_hero_status():
    f = io.StringIO()
    with safe_stdin(), redirect_stdout(f):
        exec(open("lessons/03_printing.py").read())
    output = f.getvalue()
    assert "HERO" in output.upper()


def test_uses_escape_sequences():
    with open("lessons/03_printing.py", "r") as f:
        content = f.read()
    assert "\\n" in content
    assert "\\t" in content


def test_is_valid_python():
    with open("lessons/03_printing.py", "r") as f:
        content = f.read()
    try:
        compile(content, "lessons/03_printing.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
