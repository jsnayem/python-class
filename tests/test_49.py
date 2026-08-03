"""Tests for Lesson 49: Final Integration."""
from _helpers import assert_scaffold_is_blank, count_calls, defines_function, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(49)


def test_defines_print_header():
    assert defines_function(49, "print_header"), "Step 1: define print_header(text)."


def test_print_header_shows_the_title():
    run = run_student(49)
    import io
    from contextlib import redirect_stdout

    buf = io.StringIO()
    with redirect_stdout(buf):
        run.get("print_header")("GAME START")
    assert "GAME START" in buf.getvalue(), (
        "Step 1: print_header should print the text it is given."
    )


def test_calls_load_game():
    assert count_calls(49, "load_game") >= 1, "Step 2: call load_game()."


def test_creates_a_hero_and_welcomes_them():
    run = run_student(49)
    hero = run.get("hero")
    assert hero is not None, "Step 3: create a Hero."
    assert str(getattr(hero, "name", hero)) in run.output, (
        "Step 3: print a welcome message with your hero's name."
    )
