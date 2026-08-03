"""Tests for Lesson 9: Loops (while and for)."""
import ast

from _helpers import assert_scaffold_is_blank, run_student, uses_node


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(9)


def test_uses_a_while_loop():
    assert uses_node(9, (ast.While,)), "Step 1: use a while loop to count 1 to 5."


def test_uses_a_for_loop():
    assert uses_node(9, (ast.For,)), "Step 2: use a for loop over the inventory."


def test_counts_one_to_five():
    run = run_student(9)
    for n in range(1, 6):
        assert str(n) in run.output, f"Step 1: your count should print {n}."


def test_prints_inventory_items():
    run = run_student(9)
    inv = run.get("inventory")
    assert isinstance(inv, list) and inv, "Step 2: create an inventory list."
    for item in inv:
        assert str(item).lower() in run.output.lower(), (
            f"Step 2: print each inventory item ({item} is missing)."
        )
