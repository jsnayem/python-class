"""Tests for Lesson 10: Functions."""
from _helpers import (
    assert_scaffold_is_blank,
    count_calls,
    defines_function,
    run_student,
)


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(10)


def test_defines_show_status():
    assert defines_function(10, "show_status"), (
        "Step 1: define show_status(name, health, gold)."
    )


def test_show_status_called_for_two_heroes():
    assert count_calls(10, "show_status") >= 2, (
        "Step 2: call show_status for two different heroes."
    )


def test_calculate_damage_returns_the_total():
    run = run_student(10)
    fn = run.get("calculate_damage")
    assert callable(fn), "Step 3: define calculate_damage(base, bonus)."
    assert fn(10, 5) == 15, "Step 3: calculate_damage should return base + bonus."
    assert fn(3, 0) == 3
