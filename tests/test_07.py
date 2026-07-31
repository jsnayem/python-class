"""Tests for Lesson 7: Lists"""

from _helpers import safe_stdin


def test_scaffold_has_no_answer():
    # The scaffold for this lesson must be a blank starter template
    # (marked with a TODO line), not a filled answer.
    scaffold = open("scaffolds/07_lists.py").read()
    assert "TODO: Write your code for Lesson" in scaffold


def test_list_created():
    namespace = {}
    with open("lessons/07_lists.py", "r") as f, safe_stdin():
        exec(f.read(), namespace)
    assert "inventory" in namespace


def test_uses_append():
    with open("lessons/07_lists.py", "r") as f:
        content = f.read()
    assert ".append(" in content


def test_uses_for_loop():
    with open("lessons/07_lists.py", "r") as f:
        content = f.read()
    assert "for" in content
    assert "enumerate" in content


def test_is_valid_python():
    with open("lessons/07_lists.py", "r") as f:
        content = f.read()
    try:
        compile(content, "lessons/07_lists.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
