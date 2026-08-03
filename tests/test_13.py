"""Tests for Lesson 13: For Loops."""
import ast

from _helpers import assert_scaffold_is_blank, run_student, uses_node


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(13)


def test_uses_a_for_loop():
    assert uses_node(13, (ast.For,)), "Steps 1-2: use for loops."


def test_prints_every_inventory_item():
    run = run_student(13)
    inv = run.get("inventory")
    assert isinstance(inv, list) and inv, "Step 1: create an inventory list."
    for item in inv:
        assert str(item).lower() in run.output.lower(), (
            f"Step 1: print each inventory item ({item} is missing)."
        )


def test_prints_three_numbers_from_range():
    run = run_student(13)
    digits = [ln for ln in run.output.splitlines() if any(c.isdigit() for c in ln)]
    assert len(digits) >= 3, (
        "Step 2: use for i in range(3) to print three numbers."
    )
