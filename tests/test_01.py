"""Tests for Lesson 1: Hello, World!

Graded on behaviour: the student must print three lines of their own
choosing. Their name and fun fact are personal, so we never assert on the
literal text of those.
"""
import ast

from _helpers import assert_scaffold_is_blank, count_calls, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(1)


def test_greets_the_adventurer():
    run = run_student(1)
    assert "hello" in run.output.lower(), (
        "Step 1: print a greeting that says hello."
    )


def test_prints_three_lines():
    run = run_student(1)
    lines = [ln for ln in run.output.splitlines() if ln.strip()]
    assert len(lines) >= 3, (
        f"Steps 1-3 ask for three printed lines (greeting, your name, a fun "
        f"fact); your program printed {len(lines)}."
    )


def test_uses_print():
    assert count_calls(1, "print") >= 3, "Use print() for each of the 3 steps."
