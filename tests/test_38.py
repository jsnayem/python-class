"""Tests for Lesson 38: Attack."""
from pathlib import Path

from _helpers import load_answer, lesson_text

ROOT = Path(__file__).parent.parent


def test_student_file_present():
    assert list((ROOT / "lessons").glob("38_*.py")), "Lesson 38 file should exist"


def test_student_has_attack_function():
    assert "def attack" in lesson_text(38)


def test_answer_attack_damages_monster():
    m = load_answer("38_combat_system")

    class FakeHero:
        weapon: object = None

    class FakeWeapon:
        attack_bonus = 5

    class FakeMonster:
        health = 30

        def take_damage(self, d):
            self.health -= d

    hero = FakeHero()
    hero.weapon = FakeWeapon()
    monster = FakeMonster()
    dmg = m.attack(hero, monster)
    assert dmg == 5
    assert monster.health == 25
