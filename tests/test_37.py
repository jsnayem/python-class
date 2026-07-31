"""Tests for Lesson 37: Monster Class."""
from pathlib import Path

from _helpers import load_answer

ROOT = Path(__file__).parent.parent


def test_student_file_present():
    assert list((ROOT / "lessons").glob("37_*.py")), "Lesson 37 file should exist"


def test_answer_monster_is_alive_and_takes_damage():
    m = load_answer("37_monster_class")
    goblin = m.Monster("Goblin", 30, 8, 15)
    assert goblin.is_alive() is True
    goblin.take_damage(10)
    assert goblin.health == 20
    goblin.take_damage(999)
    assert goblin.health == 0
    assert goblin.is_alive() is False
