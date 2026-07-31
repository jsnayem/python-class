"""Tests for Lesson 4: Math"""
import io
from contextlib import redirect_stdout


def test_damage_calculation():
    f = io.StringIO()
    with redirect_stdout(f):
        exec(open("lessons/04_math.py").read())
    output = f.getvalue()
    assert "8" in output


def test_healing_calculation():
    with open("lessons/04_math.py", "r") as f:
        content = f.read()
    assert "hero_health + 30" in content


def test_gold_calculation():
    with open("lessons/04_math.py", "r") as f:
        content = f.read()
    assert "hero_gold + monster_gold" in content or "hero_gold = hero_gold + monster_gold" in content


def test_uses_math_operators():
    with open("lessons/04_math.py", "r") as f:
        content = f.read()
    assert "+" in content


def test_is_valid_python():
    with open("lessons/04_math.py", "r") as f:
        content = f.read()
    try:
        compile(content, "lessons/04_math.py", "exec")
    except SyntaxError as e:
        raise AssertionError(f"Invalid Python syntax: {e}")
