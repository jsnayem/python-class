"""Tests for Lesson 22: Inheritance - Weapon Subclass."""
from _helpers import assert_scaffold_is_blank, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(22)


def test_item_stores_name_and_value():
    run = run_student(22)
    Item = run.get("Item")
    assert Item is not None, "Step 1: create the base Item class."
    item = Item("Ring", 25)
    assert item.name == "Ring" and item.value == 25, (
        "Step 1: Item(name, value) should store both on self."
    )


def test_weapon_subclasses_item():
    run = run_student(22)
    Item, Weapon = run.get("Item"), run.get("Weapon")
    assert Weapon is not None, "Step 2: create the Weapon subclass."
    assert issubclass(Weapon, Item), "Step 2: Weapon should inherit from Item."


def test_prints_the_weapon():
    run = run_student(22)
    assert run.output.strip(), "Step 3: create a Weapon and print it."
