"""Tests for Lesson 7: Lists."""
import ast

from _helpers import assert_scaffold_is_blank, run_student, uses_node


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(7)


def test_inventory_holds_both_items():
    run = run_student(7)
    inv = run.get("inventory")
    assert isinstance(inv, list), "Step 1: create a list called inventory."
    lowered = [str(i).lower() for i in inv]
    assert "health potion" in lowered, "Step 2: append \"Health Potion\"."
    assert "iron sword" in lowered, "Step 2: append \"Iron Sword\"."


def test_loops_over_the_inventory():
    assert uses_node(7, (ast.For,)), "Step 3: use a for loop over the inventory."


def test_prints_each_item_with_a_number():
    run = run_student(7)
    for item in ("Health Potion", "Iron Sword"):
        assert item.lower() in run.output.lower(), f"Step 3: print {item}."
    numbered = [
        ln for ln in run.output.splitlines()
        if any(ch.isdigit() for ch in ln) and ln.strip()
    ]
    assert len(numbered) >= 2, (
        "Step 3: print each item with a number next to it (enumerate() makes "
        "this easy, but any correct numbering passes)."
    )
