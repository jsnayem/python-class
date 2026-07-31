"""Tests for Lesson 32: Hero Stats (Starting Bonuses)."""
from pathlib import Path

from _helpers import load_answer, lesson_text

ROOT = Path(__file__).parent.parent


def test_student_file_present():
    assert list((ROOT / "lessons").glob("32_*.py")), "Lesson 32 file should exist"


def test_student_has_is_alive():
    assert "is_alive" in lesson_text(32)


def test_answer_hero_stats():
    m = load_answer("32_hero_stats")
    hero = m.Hero("Alex")
    assert hero.max_health == 100 and hero.health == 100
    assert hero.is_alive() is True
    hero.health = 0
    assert hero.is_alive() is False
