"""Tests for Lesson 1: Hello, World!"""
import io
import sys
from contextlib import redirect_stdout


def test_scaffold_has_no_answer():
    # The scaffold for this lesson must be a blank starter template
    # (begins with the "Scaffold for lesson N" docstring), not a filled answer.
    scaffold = open("scaffolds/01_hello_world.py").read()
    assert "Scaffold for lesson 01" in scaffold


def test_prints_hello_adventurer():
    with open("lessons/01_hello_world.py", "r") as f:
        content = f.read()
    assert "Hello, Adventurer!" in content
    assert "print(" in content


def test_prints_name():
    with open("lessons/01_hello_world.py", "r") as f:
        content = f.read()
    assert "My name is" in content


def test_prints_fun_fact():
    with open("lessons/01_hello_world.py", "r") as f:
        content = f.read()
    assert "love dragons" in content.lower()


def test_is_valid_python():
    with open("lessons/01_hello_world.py", "r") as f:
        content = f.read()
    try:
        compile(content, "lessons/01_hello_world.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
