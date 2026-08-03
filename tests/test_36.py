"""Tests for Lesson 36: Potion Class."""
from _helpers import assert_scaffold_is_blank, load_answer, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(36)


def test_potion_extends_item():
    run = run_student(36)
    Item, Potion = run.get("Item"), run.get("Potion")
    assert Item is not None and Potion is not None, (
        "Steps 1-2: define Item and Potion."
    )
    assert issubclass(Potion, Item), "Step 1: Potion should extend Item."


def test_potion_has_heal_amount():
    run = run_student(36)
    potion = run.get("Potion")("Health Potion", "Restores HP", 20, 30)
    assert potion.heal_amount == 30, "Step 2: store heal_amount on the Potion."
    assert potion.name == "Health Potion", (
        "Step 2: use super().__init__ so Item still sets the name."
    )


def test_prints_the_health_potion():
    run = run_student(36)
    assert "potion" in run.output.lower(), "Step 3: create and print a Health Potion."


def test_reference_potion():
    m = load_answer("36_potion_class")
    assert m.Potion("Health", "Heals", 20, 30).heal_amount == 30
