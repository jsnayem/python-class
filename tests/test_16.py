"""Tests for Lesson 16: Return Values."""
from _helpers import assert_scaffold_is_blank, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(16)


def test_calculate_heal_doubles_the_amount():
    run = run_student(16)
    fn = run.get("calculate_heal")
    assert callable(fn), "Step 1: define calculate_heal(amount)."
    assert fn(10) == 20, "Step 1: calculate_heal should return amount * 2."
    assert fn(0) == 0
    assert fn(7) == 14


def test_prints_the_result():
    run = run_student(16)
    assert run.output.strip(), "Step 2: call calculate_heal and print the result."
