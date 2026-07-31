"""Tests for Lesson 36: Potion Class."""
from pathlib import Path

from _helpers import load_answer

ROOT = Path(__file__).parent.parent


def test_student_file_present():
    assert list((ROOT / "lessons").glob("36_*.py")), "Lesson 36 file should exist"


def test_answer_potion_heal_amount():
    m = load_answer("36_potion_class")
    potion = m.Potion("Health Potion", "Restores HP", 20, 30)
    assert potion.heal_amount == 30
    assert isinstance(potion, m.Item)
