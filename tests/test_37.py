"""Tests for Lesson 37: Monster Class."""
from _helpers import assert_scaffold_is_blank, defines_class, load_answer, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(37)


def test_defines_monster_class():
    assert defines_class(37, "Monster"), (
        "Step 1: create Monster(name, health, attack_power, gold_reward)."
    )


def test_monster_stores_its_stats():
    run = run_student(37)
    goblin = run.get("Monster")("Goblin", 30, 8, 15)
    assert goblin.name == "Goblin"
    assert goblin.health == 30
    assert goblin.attack_power == 8
    assert goblin.gold_reward == 15


def test_take_damage_and_is_alive():
    run = run_student(37)
    goblin = run.get("Monster")("Goblin", 30, 8, 15)
    assert goblin.is_alive() is True, "Step 2: is_alive() is True while health > 0."
    goblin.take_damage(10)
    assert goblin.health == 20, "Step 2: take_damage should subtract the damage."
    goblin.take_damage(999)
    assert goblin.health == 0, "Step 2: health should never drop below 0."
    assert goblin.is_alive() is False


def test_prints_the_goblin():
    run = run_student(37)
    assert "goblin" in run.output.lower(), "Step 3: create a goblin and print its HP."


def test_reference_monster():
    m = load_answer("37_monster_class")
    assert m.Monster("Goblin", 30, 8, 15).is_alive() is True
