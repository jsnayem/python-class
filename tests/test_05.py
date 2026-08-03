"""Tests for Lesson 5: Strings."""
from _helpers import assert_scaffold_is_blank, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(5)


def test_monster_strings_created():
    run = run_student(5)
    assert isinstance(run.get("monster_name"), str), "Step 1: create monster_name."
    assert isinstance(run.get("monster_desc"), str), "Step 1: create monster_desc."


def test_prints_upper_and_lower_versions():
    run = run_student(5)
    name = run.get("monster_name", "")
    assert name.upper() in run.output, "Step 3: print monster_name.upper()."
    assert name.lower() in run.output, "Step 3: print monster_name.lower()."


def test_combines_name_and_description():
    run = run_student(5)
    name = run.get("monster_name", "")
    desc = run.get("monster_desc", "")
    combined = [
        ln for ln in run.output.splitlines()
        if name.lower() in ln.lower() and desc.lower() in ln.lower()
    ]
    assert combined, (
        "Step 2: print one message that contains both the monster's name and "
        "its description."
    )
