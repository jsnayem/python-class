"""Tests for Lesson 35: Weapon Class (and Potion)."""
from _helpers import assert_scaffold_is_blank, load_answer, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(35)


def test_subclasses_inherit_from_item():
    run = run_student(35)
    Item, Weapon, Potion = run.get("Item"), run.get("Weapon"), run.get("Potion")
    assert Item is not None, "Step 1: define the base Item class."
    assert Weapon is not None and issubclass(Weapon, Item), (
        "Step 2: Weapon should inherit from Item."
    )
    assert Potion is not None and issubclass(Potion, Item), (
        "Step 2: Potion should inherit from Item."
    )


def test_weapon_and_potion_carry_their_extra_stat():
    run = run_student(35)
    weapon = run.get("Weapon")("Sword", "A blade", 50, 5)
    potion = run.get("Potion")("Health", "Heals", 20, 30)
    assert weapon.attack_bonus == 5, "Step 2: Weapon needs an attack_bonus."
    assert potion.heal_amount == 30, "Step 2: Potion needs a heal_amount."
    assert weapon.name == "Sword" and weapon.value == 50, (
        "Step 2: call super().__init__ so Item still sets name/description/value."
    )


def test_prints_both():
    run = run_student(35)
    assert run.output.strip(), "Step 3: create both and print them."


def test_reference_subclasses():
    m = load_answer("35_weapon_class")
    assert issubclass(m.Weapon, m.Item)
