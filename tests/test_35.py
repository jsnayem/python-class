"""Tests for Lesson 35: Weapon and Potion (subclasses of Item)."""
from pathlib import Path

from _helpers import load_answer

ROOT = Path(__file__).parent.parent


def test_student_file_present():
    assert list((ROOT / "lessons").glob("35_*.py")), "Lesson 35 file should exist"


def test_answer_subclasses_inherit_item():
    m = load_answer("35_weapon_class")
    w = m.Weapon("Sword", "A blade", 50, 5)
    p = m.Potion("Health", "Heals", 20, 30)
    assert isinstance(w, m.Item) and isinstance(p, m.Item)
    assert w.attack_bonus == 5 and p.heal_amount == 30
