"""Tests for Lesson 47: Decorative UI."""
from _helpers import assert_scaffold_is_blank, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(47)


def test_prints_a_title_border():
    run = run_student(47)
    lines = [ln.strip() for ln in run.output.splitlines() if ln.strip()]
    borders = [
        ln for ln in lines
        if len(ln) >= 5 and len(set(ln)) <= 2 and not any(c.isalnum() for c in ln)
    ]
    assert borders, (
        "Step 1: print a fancy border line (a row of the same character, e.g. "
        "'====' or '****')."
    )


def test_has_a_title_between_separators():
    run = run_student(47)
    lines = [ln.strip() for ln in run.output.splitlines() if ln.strip()]
    assert len(lines) >= 3, (
        "Steps 1-2: print a border, a title, and a separator line."
    )
    assert any(any(c.isalpha() for c in ln) for ln in lines), (
        "Step 1: your banner needs a title with words in it."
    )
