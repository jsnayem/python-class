"""Tests for Lesson 39: Damage Formula."""
from _helpers import assert_scaffold_is_blank, defines_function, load_answer, run_student


class _Fighter:
    def __init__(self, attack_power=10, defense=0):
        self.attack_power = attack_power
        self.defense = defense


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(39)


def test_defines_calculate_damage():
    assert defines_function(39, "calculate_damage"), (
        "Step 1: define calculate_damage(attacker, defender)."
    )


def test_damage_is_power_minus_defense():
    run = run_student(39)
    fn = run.get("calculate_damage")
    assert fn(_Fighter(10, 0), _Fighter(10, 0)) == 10
    assert fn(_Fighter(12, 4), _Fighter(10, 4)) == 8


def test_damage_never_drops_below_one():
    run = run_student(39)
    fn = run.get("calculate_damage")
    assert fn(_Fighter(3, 0), _Fighter(10, 10)) == 1, (
        "Step 2: a hit always deals at least 1 damage."
    )


def test_reference_damage():
    m = load_answer("39_attack_logic")
    assert m.calculate_damage(_Fighter(3, 10), _Fighter(3, 10)) == 1
