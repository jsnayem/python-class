"""Tests for Lesson 23: Inheritance - Shop Items."""
from _helpers import assert_scaffold_is_blank, load_answer, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(23)


def test_weapon_and_potion_inherit_from_item():
    run = run_student(23)
    Item, Weapon, Potion = run.get("Item"), run.get("Weapon"), run.get("Potion")
    assert Item is not None, "Step 1: define the base Item class."
    assert Weapon is not None and issubclass(Weapon, Item), (
        "Step 1: Weapon should inherit from Item."
    )
    assert Potion is not None and issubclass(Potion, Item), (
        "Step 1: Potion should inherit from Item."
    )


def test_children_reuse_the_parent_initialiser():
    run = run_student(23)
    Weapon = run.get("Weapon")
    weapon = Weapon("Sword", 50, 5)
    assert weapon.name == "Sword" and weapon.price == 50, (
        "Step 2: call super().__init__ so the parent sets name and price."
    )


def test_prints_both_items():
    run = run_student(23)
    assert run.output.strip(), "Step 3: create one Weapon and one Potion, print both."


def test_reference_potion_carries_amount():
    m = load_answer("23_inheritance")
    assert m.Potion("Health", 20, 30).amount == 30
