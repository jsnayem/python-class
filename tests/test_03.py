"""Tests for Lesson 3: Printing with Style."""
from _helpers import assert_scaffold_is_blank, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(3)


def test_prints_a_title_border():
    run = run_student(3)
    assert "==" in run.output, "Step 1: print a title border made of '=' characters."


def test_uses_a_tab_and_a_newline_escape():
    run = run_student(3)
    assert "\t" in run.output, "Step 2: use \\t somewhere in your output."
    blank_lines = [ln for ln in run.output.split("\n") if not ln.strip()]
    assert blank_lines, "Step 2: use \\n to create a blank line in your output."


def test_prints_hero_stats_on_one_line():
    run = run_student(3)
    lines = [ln for ln in run.output.splitlines() if ln.strip()]
    assert any(
        sum(ch.isdigit() for ch in ln) >= 2 for ln in lines
    ), "Step 3: print the hero name, health and gold together on one line."
