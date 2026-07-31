"""Tests for Lesson 33: Hero Inventory."""
from pathlib import Path

from _helpers import load_answer, lesson_text

ROOT = Path(__file__).parent.parent


def test_student_file_present():
    assert list((ROOT / "lessons").glob("33_*.py")), "Lesson 33 file should exist"


def test_student_has_add_item():
    assert "add_item" in lesson_text(33)


def test_answer_inventory_add_drop():
    m = load_answer("33_hero_inventory")
    hero = m.Hero("Alex")
    hero.add_item("sword")
    assert "sword" in hero.inventory
    hero.drop_item("sword")
    assert "sword" not in hero.inventory
