"""Tests for Lesson 10: Functions"""


def test_scaffold_has_no_answer():
    # The scaffold for this lesson must be a blank starter template
    # (marked with a TODO line), not a filled answer.
    scaffold = open("scaffolds/10_functions.py").read()
    assert "TODO: Write your code for Lesson" in scaffold


def test_is_valid_python():
    with open("lessons/10_functions.py", "r") as f:
        content = f.read()
    try:
        compile(content, "lessons/10_functions.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
