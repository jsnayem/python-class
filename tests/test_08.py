"""Tests for Lesson 8: If Statements."""
import ast

from _helpers import assert_scaffold_is_blank, run_student, uses_node


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(8)


def test_health_and_gold_variables_exist():
    run = run_student(8)
    assert isinstance(run.get("health"), (int, float)), "Step 1: create health."
    assert isinstance(run.get("gold"), (int, float)), "Step 1: create gold."


def test_uses_a_comparison_in_an_if():
    assert uses_node(8, (ast.If,)), "Steps 2-3: use if statements."
    assert uses_node(8, (ast.Compare,)), (
        "Steps 2-3: compare health and gold with < or >."
    )


def test_low_health_warning_triggers():
    run = run_student(8)
    if run.get("health", 100) < 20:
        assert run.output.strip(), "Step 2: print a warning when health < 20."


def test_program_prints_something():
    run = run_student(8)
    assert run.output.strip(), (
        "Your program should print at least one message for the health or "
        "gold check."
    )
