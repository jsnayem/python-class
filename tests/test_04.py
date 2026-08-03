"""Tests for Lesson 4: Math."""
from _helpers import assert_scaffold_is_blank, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(4)


def test_damage_is_attack_minus_defense():
    run = run_student(4)
    assert "damage" in run, "Step 1: store the result in a variable called damage."
    attack = run.get("hero_attack")
    defense = run.get("monster_defense")
    assert isinstance(attack, (int, float)), "Step 1: create hero_attack."
    assert isinstance(defense, (int, float)), "Step 1: create monster_defense."
    assert run.get("damage") == attack - defense, (
        "Step 1: damage should equal hero_attack - monster_defense."
    )


def test_healing_adds_thirty():
    run = run_student(4)
    assert "hero_health" in run, "Step 2: create hero_health."
    assert run.get("hero_health") == 130, (
        f"Step 2: after adding 30 to a starting health of 100, hero_health "
        f"should be 130, got {run.get('hero_health')!r}."
    )


def test_gold_gains_the_monster_reward():
    run = run_student(4)
    gold = run.get("hero_gold")
    reward = run.get("monster_gold")
    assert isinstance(reward, (int, float)), "Step 3: create monster_gold."
    assert isinstance(gold, (int, float)), "Step 3: create hero_gold."
    assert gold >= reward, "Step 3: add monster_gold to hero_gold."
