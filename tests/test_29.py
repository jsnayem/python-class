"""Tests for Lesson 29: Time and Delays."""
from _helpers import assert_scaffold_is_blank, count_calls, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(29)


def test_uses_sleep_for_the_dramatic_pause():
    assert count_calls(29, "sleep") >= 1, "Step 1: use time.sleep() between prints."


def test_measures_elapsed_time():
    assert count_calls(29, "time") >= 2, (
        "Step 2: call time.time() before and after to measure elapsed time."
    )


def test_prints_a_sequence_and_an_elapsed_value():
    run = run_student(29)
    lines = [ln for ln in run.output.splitlines() if ln.strip()]
    assert len(lines) >= 2, "Step 1: print a dramatic multi-line sequence."
    assert any(any(c.isdigit() for c in ln) for ln in lines), (
        "Step 2: print how long it took."
    )
