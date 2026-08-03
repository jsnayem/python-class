"""Tests for Lesson 32: Hero Stats - Starting Bonuses."""
from _helpers import assert_scaffold_is_blank, load_answer, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(32)


def test_hero_has_max_health():
    run = run_student(32)
    hero = run.get("Hero")("Alex")
    assert hero.max_health == 100, "Step 1: add max_health (100) in __init__."
    assert hero.health == hero.max_health, "Step 1: a new hero starts at full health."


def test_is_alive_reflects_health():
    run = run_student(32)
    hero = run.get("Hero")("Alex")
    assert hero.is_alive() is True, "Step 2: is_alive() is True while health > 0."
    hero.health = 0
    assert hero.is_alive() is False, "Step 2: is_alive() is False at 0 health."


def test_prints_both_states():
    run = run_student(32)
    assert run.output.strip(), "Step 3: print the alive and dead states."


def test_reference_hero_stats():
    m = load_answer("32_hero_stats")
    hero = m.Hero("Alex")
    assert hero.is_alive() is True
