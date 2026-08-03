"""Tests for Lesson 18: Tuples."""
from _helpers import assert_scaffold_is_blank, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(18)


def test_weapon_tuple_exists():
    run = run_student(18)
    weapon = run.get("weapon")
    assert isinstance(weapon, tuple), "Step 1: create a tuple called weapon."
    assert len(weapon) >= 2, "Step 1: the weapon tuple needs at least 2 values."


def test_prints_both_elements():
    run = run_student(18)
    weapon = run.get("weapon", ())
    for value in weapon[:2]:
        assert str(value).lower() in run.output.lower(), (
            f"Step 2: print weapon[0] and weapon[1] ({value} is missing)."
        )
