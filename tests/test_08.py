"""Tests for Lesson 8: If Statements"""
import io
from contextlib import redirect_stdout

from _helpers import safe_stdin


def test_low_health_warning():
    f = io.StringIO()
    with safe_stdin(), redirect_stdout(f):
        exec(open("lessons/08_if_statements.py").read())
    output = f.getvalue()
    assert "health" in output.lower() or "warning" in output.lower()


def test_wealthy_message():
    f = io.StringIO()
    with safe_stdin(), redirect_stdout(f):
        exec(open("lessons/08_if_statements.py").read())
    output = f.getvalue()
    assert "gold" in output.lower() or "rich" in output.lower()


def test_combined_condition():
    f = io.StringIO()
    with safe_stdin(), redirect_stdout(f):
        exec(open("lessons/08_if_statements.py").read())
    output = f.getvalue()
    assert output.strip() != ""


def test_uses_and_operator():
    with open("lessons/08_if_statements.py", "r") as f:
        content = f.read()
    assert "and" in content


def test_uses_comparison_operators():
    with open("lessons/08_if_statements.py", "r") as f:
        content = f.read()
    assert "<" in content or ">" in content or "==" in content
