"""Tests for Lesson 23: Inheritance (Shop Items).

Validates real subclass behavior against the answer_key/ reference.
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).parent.parent


def _load_answer(modname):
    spec = importlib.util.spec_from_file_location(
        modname, ROOT / "answer_key" / f"{modname}.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_student_file_present():
    assert list((ROOT / "lessons").glob("23_*.py")), "Lesson 23 file should exist"


def test_student_uses_super():
    text = (ROOT / "lessons" / next((ROOT / "lessons").glob("23_*.py")).name).read_text()
    assert "super()" in text, "Subclasses should call super().__init__()"


def test_answer_weapon_carries_bonus():
    m = _load_answer("23_inheritance")
    w = m.Weapon("Sword", 50, 5)
    assert isinstance(w, m.Item)
    assert w.name == "Sword" and w.price == 50 and w.bonus == 5


def test_answer_potion_carries_amount():
    m = _load_answer("23_inheritance")
    p = m.Potion("Health", 20, 30)
    assert isinstance(p, m.Item)
    assert p.amount == 30
