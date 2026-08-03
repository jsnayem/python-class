"""Tests for Lesson 40: Flee Mechanic."""
from _helpers import assert_scaffold_is_blank, defines_function, load_answer, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(40)


def test_defines_flee():
    assert defines_function(40, "flee"), "Step 1: define flee(chance=0.5)."


def test_flee_returns_a_bool():
    run = run_student(40)
    fn = run.get("flee")
    results = {fn() for _ in range(60)}
    assert results <= {True, False}, "Step 1: flee() should return True or False."


def test_flee_respects_the_chance():
    run = run_student(40)
    fn = run.get("flee")
    assert fn(chance=1.0) is True, "Step 2: a chance of 1.0 always escapes."
    assert fn(chance=0.0) is False, "Step 2: a chance of 0.0 never escapes."


def test_flee_is_random():
    run = run_student(40)
    fn = run.get("flee")
    results = {fn() for _ in range(80)}
    assert results == {True, False}, (
        "Step 2: use random so the outcome actually varies."
    )


def test_reference_flee():
    m = load_answer("40_flee_mechanic")
    assert m.flee(chance=1.0) is True
