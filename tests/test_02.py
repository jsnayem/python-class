"""Tests for Lesson 2: Variables"""
import io
from contextlib import redirect_stdout


def test_scaffold_has_no_answer():
    scaffold = open("scaffolds/02_starter.py").read()
    assert "hero_name" not in scaffold
    assert "hero_health" not in scaffold
    assert "hero_gold" not in scaffold


def test_variables_exist():
    with open("lessons/02_variables.py", "r") as f:
        content = f.read()
    assert "hero_name" in content
    assert "hero_health" in content
    assert "hero_gold" in content


def test_gold_increases():
    with open("lessons/02_variables.py", "r") as f:
        content = f.read()
    assert "hero_gold + 20" in content
    assert "gold after finding treasure" in content.lower()


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
