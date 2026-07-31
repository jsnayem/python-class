"""Tests for Lesson 39: Combat Loop (damage formula)."""
from pathlib import Path

from _helpers import load_answer, lesson_text

ROOT = Path(__file__).parent.parent


def test_student_file_present():
    assert list((ROOT / "lessons").glob("39_*.py")), "Lesson 39 file should exist"


def test_student_has_calculate_damage():
    assert "calculate_damage" in lesson_text(39)


def test_answer_damage_minimum_one():
    m = load_answer("39_attack_logic")

    class Fighter:
        attack_power = 10
        defense = 0

    weak = Fighter()
    weak.attack_power = 3
    weak.defense = 10
    assert m.calculate_damage(weak, weak) == 1  # never less than 1
    assert m.calculate_damage(Fighter(), Fighter()) == 10
