"""Tests for Lesson 10: Functions"""


def test_scaffold_has_no_answer():
    scaffold = open("scaffolds/10_starter.py").read()
    assert "show_status" not in scaffold
    assert "calculate_damage" not in scaffold


def test_is_valid_python():
    with open("lessons/10_functions.py", "r") as f:
        content = f.read()
    try:
        compile(content, "lessons/10_functions.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
