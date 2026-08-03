"""Tests for Lesson 50: Play and Share."""
from _helpers import assert_scaffold_is_blank, count_calls, defines_function, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(50)


def test_prints_a_completion_message():
    run = run_student(50)
    assert run.output.strip(), "Step 1: print a completion message."


def test_defines_and_calls_credits():
    assert defines_function(50, "credits"), "Step 2: define a credits() function."
    assert count_calls(50, "credits") >= 1, "Step 2: call credits()."


def test_credits_print_something():
    run = run_student(50)
    import io
    from contextlib import redirect_stdout

    buf = io.StringIO()
    with redirect_stdout(buf):
        run.get("credits")()
    assert buf.getvalue().strip(), "Step 2: credits() should print your credits."


def test_says_something_proud():
    run = run_student(50)
    lines = [ln for ln in run.output.splitlines() if ln.strip()]
    assert len(lines) >= 3, (
        "Step 3: finish with a few proud statements about what you built."
    )
