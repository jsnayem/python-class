"""Tests for Lesson 28: Randomness."""
from _helpers import assert_scaffold_is_blank, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(28)


def test_roll_dice_stays_in_range():
    run = run_student(28)
    roll = run.get("roll_dice")
    assert callable(roll), "Step 1: define roll_dice(sides=6)."
    results = {roll() for _ in range(60)}
    assert results <= set(range(1, 7)), (
        f"Step 1: a 6-sided die should only return 1-6, saw {sorted(results)}."
    )
    assert len(results) > 1, "Step 1: use random so the roll actually varies."


def test_roll_dice_honours_the_sides_argument():
    run = run_student(28)
    roll = run.get("roll_dice")
    results = {roll(20) for _ in range(80)}
    assert results <= set(range(1, 21)), "Step 1: respect the sides argument."
    assert max(results) > 6, "Step 1: roll_dice(20) should be able to exceed 6."


def test_random_loot_returns_something():
    run = run_student(28)
    loot = run.get("random_loot")
    assert callable(loot), "Step 3: define random_loot()."
    assert loot() is not None, "Step 3: random_loot should return an item."


def test_prints_three_rolls():
    run = run_student(28)
    lines = [ln for ln in run.output.splitlines() if any(c.isdigit() for c in ln)]
    assert len(lines) >= 3, "Step 2: print 3 dice rolls."
