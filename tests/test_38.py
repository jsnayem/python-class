"""Tests for Lesson 38: Combat System - Attack."""
from _helpers import assert_scaffold_is_blank, defines_function, load_answer, run_student


class _Weapon:
    attack_bonus = 5


class _Monster:
    def __init__(self, health=30):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        return damage


class _Hero:
    def __init__(self, weapon=None):
        self.weapon = weapon


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(38)


def test_defines_attack():
    assert defines_function(38, "attack"), "Step 1: define attack(hero, monster)."


def test_attack_uses_the_weapon_bonus():
    run = run_student(38)
    monster = _Monster()
    damage = run.get("attack")(_Hero(_Weapon()), monster)
    assert damage == 5, "Step 2: an armed hero deals the weapon's attack_bonus."
    assert monster.health == 25, "Step 3: call monster.take_damage(damage)."


def test_unarmed_hero_still_deals_one_damage():
    run = run_student(38)
    monster = _Monster()
    damage = run.get("attack")(_Hero(None), monster)
    assert damage == 1, "Step 2: with no weapon the damage is 1."
    assert monster.health == 29


def test_reference_attack():
    m = load_answer("38_combat_system")
    monster = _Monster()
    assert m.attack(_Hero(_Weapon()), monster) == 5
