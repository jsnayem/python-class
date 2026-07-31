"""Tests for Lesson 6: Input"""


def test_input_exists():
    with open("lessons/06_input.py", "r") as f:
        content = f.read()
    assert "input(" in content


def test_has_if_statement():
    with open("lessons/06_input.py", "r") as f:
        content = f.read()
    assert "if " in content


def test_handles_attack_choice():
    with open("lessons/06_input.py", "r") as f:
        content = f.read()
    assert '"a"' in content or "'a'" in content


def test_handles_flee_choice():
    with open("lessons/06_input.py", "r") as f:
        content = f.read()
    assert '"f"' in content or "'f'" in content


def test_is_valid_python():
    with open("lessons/06_input.py", "r") as f:
        content = f.read()
    try:
        compile(content, "lessons/06_input.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
