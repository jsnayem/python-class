"""Tests for Lesson 14: Functions Intro."""
from _helpers import assert_scaffold_is_blank, count_calls, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(14)


def test_defines_cast_spell():
    run = run_student(14)
    assert callable(run.get("cast_spell")), "Step 1: define cast_spell(spell_name)."


def test_called_three_times():
    assert count_calls(14, "cast_spell") >= 3, (
        "Step 2: call cast_spell three times with different spells."
    )


def test_prints_three_spell_messages():
    run = run_student(14)
    lines = [ln for ln in run.output.splitlines() if ln.strip()]
    assert len(lines) >= 3, (
        f"Step 2: three calls should print three messages; got {len(lines)}."
    )
