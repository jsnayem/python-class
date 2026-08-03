"""Tests for Lesson 24: Error Handling - Safe Input."""
import ast

from _helpers import assert_scaffold_is_blank, run_student, uses_node


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(24)


def test_uses_try_except():
    assert uses_node(24, (ast.Try,)), "Step 1: use try/except."


def test_safe_int_parses_a_number(monkeypatch=None):
    run = run_student(24)
    fn = run.get("safe_int")
    assert callable(fn), "Step 1: define safe_int(prompt)."
    import builtins

    original = builtins.input
    try:
        builtins.input = lambda *_: "42"
        assert fn("Number? ") == 42, "safe_int should return the number typed."
        builtins.input = lambda *_: "not a number"
        assert fn("Number? ") == 0, "Step 2: return 0 when the input is not a number."
    finally:
        builtins.input = original


def test_prints_an_error_message_on_bad_input():
    run = run_student(24)
    import builtins
    import io
    from contextlib import redirect_stdout

    fn = run.get("safe_int")
    original = builtins.input
    buf = io.StringIO()
    try:
        builtins.input = lambda *_: "oops"
        with redirect_stdout(buf):
            fn("Number? ")
    finally:
        builtins.input = original
    assert buf.getvalue().strip(), "Step 2: print an error message on bad input."
