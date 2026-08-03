"""Tests for Lesson 34: Item Class - Base."""
from _helpers import assert_scaffold_is_blank, defines_class, load_answer, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(34)


def test_defines_item_class():
    assert defines_class(34, "Item"), (
        "Step 1: create Item(name, description, value)."
    )


def test_item_stores_all_three_values():
    run = run_student(34)
    item = run.get("Item")("Ring", "A shiny ring", 25)
    assert item.name == "Ring", "Step 1: store the name."
    assert item.description == "A shiny ring", "Step 1: store the description."
    assert item.value == 25, "Step 1: store the value."


def test_prints_the_item():
    run = run_student(34)
    assert run.output.strip(), "Step 2: create an Item and print it."


def test_reference_item_attributes():
    m = load_answer("34_item_class")
    assert m.Item("Ring", "A shiny ring", 25).value == 25
