"""Tests for Lesson 48: Objectives."""
from _helpers import assert_scaffold_is_blank, defines_function, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(48)


def test_objectives_is_a_list_of_tuples():
    run = run_student(48)
    objectives = run.get("objectives")
    assert isinstance(objectives, list) and objectives, (
        "Step 1: create a list called objectives."
    )
    assert all(isinstance(o, tuple) and len(o) >= 2 for o in objectives), (
        "Step 1: each objective is a tuple of (description, done)."
    )
    done_flags = {bool(o[1]) for o in objectives}
    assert done_flags == {True, False}, (
        "Step 3: include at least one finished and one unfinished objective."
    )


def test_show_objectives_marks_done_and_not_done():
    assert defines_function(48, "show_objectives"), (
        "Step 2: define show_objectives(objectives)."
    )
    run = run_student(48)
    for text, _done in run.get("objectives"):
        assert str(text).lower() in run.output.lower(), (
            f"Step 2: print every objective ({text} is missing)."
        )
    marks = {ln.strip()[:3] for ln in run.output.splitlines() if ln.strip()}
    assert len(marks) >= 2, (
        "Step 3: show finished and unfinished objectives differently (e.g. "
        "[x] and [ ])."
    )
