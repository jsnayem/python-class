"""Tests for Lesson 11: Functions - Making a Spell."""
from _helpers import assert_scaffold_is_blank, count_calls, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(11)


def test_defines_cast_fireball():
    run = run_student(11)
    assert callable(run.get("cast_fireball")), (
        "Step 1: define cast_fireball(damage)."
    )


def test_cast_fireball_takes_a_damage_argument():
    run = run_student(11)
    import inspect

    params = inspect.signature(run.get("cast_fireball")).parameters
    assert len(params) >= 1, "Step 1: cast_fireball needs a damage parameter."


def test_called_with_different_damage_amounts():
    assert count_calls(11, "cast_fireball") >= 2, (
        "Step 2: call cast_fireball with different damage amounts."
    )


def test_prints_a_fireball_message():
    run = run_student(11)
    assert "fireball" in run.output.lower(), (
        "Step 1: the message should mention the fireball."
    )
