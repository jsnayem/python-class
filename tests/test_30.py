"""Tests for Lesson 30: F-Strings and Formatting."""
import ast

from _helpers import assert_scaffold_is_blank, run_student, uses_node


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(30)


def test_uses_an_f_string():
    assert uses_node(30, (ast.JoinedStr,)), (
        "Step 2: build your table with f-strings."
    )


def test_hero_variables_exist():
    run = run_student(30)
    assert isinstance(run.get("hero"), str), "Step 1: create a hero variable."
    assert run.get("hp") is not None, "Step 1: create an hp variable."
    assert run.get("gold") is not None, "Step 1: create a gold variable."


def test_prints_an_aligned_table_with_the_values():
    run = run_student(30)
    out = run.output
    for name in ("hero", "hp", "gold"):
        assert str(run.get(name)) in out, f"Step 2: show the {name} value."
    lines = [ln for ln in out.splitlines() if ln.strip()]
    assert len(lines) >= 2, "Step 2: print a table with at least two rows."
