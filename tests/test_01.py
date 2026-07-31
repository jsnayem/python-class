"""Tests for Lesson 1: Hello, World!"""
import io
import sys
from contextlib import redirect_stdout


def test_scaffold_has_no_answer():
    scaffold = open("scaffolds/01_starter.py").read()
    assert "Hello, Adventurer!" not in scaffold
    assert "My name is" not in scaffold
    assert "love dragons" not in scaffold.lower()


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
