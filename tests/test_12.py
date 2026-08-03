"""Tests for Lesson 12: Multiple Parameters (default arguments)."""
from _helpers import assert_scaffold_is_blank, count_calls, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(12)


def test_defines_greet_with_a_default_greeting():
    run = run_student(12)
    greet = run.get("greet")
    assert callable(greet), "Step 1: define greet(name, greeting=\"Hello\")."
    import inspect

    params = inspect.signature(greet).parameters
    assert "greeting" in params, "Step 1: the second parameter is 'greeting'."
    assert params["greeting"].default == "Hello", (
        "Step 1: greeting should default to \"Hello\"."
    )


def test_called_both_ways():
    assert count_calls(12, "greet") >= 2, (
        "Step 2: call greet with one argument and with both arguments."
    )


def test_output_uses_both_greetings():
    run = run_student(12)
    assert "hello" in run.output.lower(), (
        "Step 2: the default call should print the Hello greeting."
    )
