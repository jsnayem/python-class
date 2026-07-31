"""Tests for Lesson 2: Variables"""
import io
from contextlib import redirect_stdout


def test_scaffold_has_no_answer():
    # The scaffold for this lesson must be a blank starter template
    # (marked with a TODO line), not a filled answer.
    scaffold = open("scaffolds/02_variables.py").read()
    assert "TODO: Write your code for Lesson" in scaffold


def test_variables_exist():
    with open("lessons/02_variables.py", "r") as f:
        content = f.read()
    assert "hero_name" in content
    assert "hero_health" in content
    assert "hero_gold" in content


def test_gold_increases():
    with open("lessons/02_variables.py", "r") as f:
        content = f.read()
    # The lesson asks to add 20 to hero_gold.
    assert "hero_gold + 20" in content
    # Execute the student code and verify the gold actually increased to 70
    # (50 starting gold + 20), rather than matching a brittle label string.
    ns: dict = {}
    with redirect_stdout(io.StringIO()):
        exec(compile(content, "lessons/02_variables.py", "exec"), ns)
    assert ns.get("hero_gold") == 70, (
        f"hero_gold should be 70 after adding 20 to 50, "
        f"got {ns.get('hero_gold')!r}"
    )


def test_uses_f_strings():
    with open("lessons/02_variables.py", "r") as f:
        content = f.read()
    assert 'f"' in content or "f'" in content


def test_is_valid_python():
    with open("lessons/02_variables.py", "r") as f:
        content = f.read()
    try:
        compile(content, "lessons/02_variables.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
