"""Tests for Lesson 46: Color System."""
from _helpers import assert_scaffold_is_blank, defines_class, defines_function, run_student

ESC = "\033"


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(46)


def test_defines_color_class_with_escape_codes():
    assert defines_class(46, "Color"), "Step 1: create the Color class."
    run = run_student(46)
    Color = run.get("Color")
    codes = [
        v for k, v in vars(Color).items()
        if not k.startswith("__") and isinstance(v, str)
    ]
    assert codes, "Step 1: Color needs escape-code constants."
    assert any(ESC in c for c in codes), (
        "Step 1: the constants should be ANSI escape codes (they start with "
        "\\033)."
    )
    assert hasattr(Color, "RESET"), "Step 1: include a RESET code."


def test_colorize_wraps_and_resets():
    assert defines_function(46, "colorize"), "Step 2: define colorize(text, color)."
    run = run_student(46)
    Color = run.get("Color")
    result = run.get("colorize")("hi", Color.RED if hasattr(Color, "RED") else Color.RESET)
    assert "hi" in result, "Step 2: colorize should keep the original text."
    assert result.endswith(Color.RESET), (
        "Step 2: colorize should end with Color.RESET so later text is normal."
    )


def test_prints_a_colored_message():
    run = run_student(46)
    assert ESC in run.output, "Step 3: print a colored message."
