"""Tests for Lesson 34: Item Class (Base)."""
from pathlib import Path

from _helpers import load_answer, lesson_text

ROOT = Path(__file__).parent.parent


def test_student_file_present():
    assert list((ROOT / "lessons").glob("34_*.py")), "Lesson 34 file should exist"


def test_student_has_item_class():
    assert "class Item" in lesson_text(34)


def test_answer_item_attributes():
    m = load_answer("34_item_class")
    item = m.Item("Ring", "A shiny ring", 25)
    assert item.name == "Ring"
    assert item.value == 25
