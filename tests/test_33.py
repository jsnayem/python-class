"""Tests for Lesson 33: Hero Inventory."""
from _helpers import assert_scaffold_is_blank, load_answer, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(33)


def test_hero_starts_with_an_empty_inventory():
    run = run_student(33)
    hero = run.get("Hero")("Alex")
    assert hero.inventory == [], "Step 1: self.inventory starts as an empty list."


def test_each_hero_has_its_own_inventory():
    run = run_student(33)
    Hero = run.get("Hero")
    a, b = Hero("A"), Hero("B")
    a.add_item("sword")
    assert b.inventory == [], (
        "Step 1: create the list inside __init__ so heroes don't share it."
    )


def test_add_and_drop_item():
    run = run_student(33)
    hero = run.get("Hero")("Alex")
    hero.add_item("sword")
    assert "sword" in hero.inventory, "Step 2: add_item should append the item."
    hero.drop_item("sword")
    assert "sword" not in hero.inventory, "Step 2: drop_item should remove the item."


def test_reference_inventory():
    m = load_answer("33_hero_inventory")
    hero = m.Hero("Alex")
    hero.add_item("sword")
    assert "sword" in hero.inventory
