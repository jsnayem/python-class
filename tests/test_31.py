"""Tests for Lesson 31: Build the Hero Class."""
from _helpers import assert_scaffold_is_blank, defines_class, load_answer, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(31)


def test_defines_hero_class():
    assert defines_class(31, "Hero"), "Step 1: create the Hero class."


def test_hero_starts_with_the_standard_stats():
    run = run_student(31)
    hero = run.get("Hero")("Alex")
    assert hero.name == "Alex", "Step 1: store the name on self.name."
    assert hero.health == 100, "Step 1: a new Hero starts with 100 health."
    assert hero.gold == 50, "Step 1: a new Hero starts with 50 gold."


def test_prints_the_hero_stats():
    run = run_student(31)
    out = run.output
    assert "100" in out and "50" in out, "Step 2: print your hero's stats."


def test_reference_hero_matches():
    m = load_answer("31_hero_class")
    hero = m.Hero("Alex")
    assert (hero.health, hero.gold) == (100, 50)
