"""Tests for Lesson 31: Build the Hero Class.

Validates real Hero behavior against the answer_key/ reference.
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
    assert list((ROOT / "lessons").glob("31_*.py")), "Lesson 31 file should exist"


def test_student_has_hero_class():
    text = (ROOT / "lessons" / next((ROOT / "lessons").glob("31_*.py")).name).read_text()
    assert "class Hero" in text


def test_answer_hero_has_name_health_gold():
    m = _load_answer("31_hero_class")
    hero = m.Hero("Alex")
    assert hero.name == "Alex"
    assert hero.health == 100, "Hero should start with 100 HP"
    assert hero.gold == 50, "Hero should start with 50 gold"
