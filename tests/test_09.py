"""Tests for Lesson 9: Loops"""


def test_is_valid_python():
    with open("lessons/09_loops.py", "r") as f:
        content = f.read()
    try:
        compile(content, "lessons/09_loops.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
