"""Tests for Lesson 6: Input.

The student's file is run with an empty stdin, so every input() returns "".
We check that input is used and that the program reacts to a choice, without
demanding particular letter codes.
"""
from _helpers import assert_scaffold_is_blank, count_calls, run_student, uses_node
import ast


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(6)


def test_asks_for_two_inputs():
    assert count_calls(6, "input") >= 2, (
        "Steps 1-2: ask for the hero name and for an action, using input() twice."
    )


def test_branches_on_the_choice():
    assert uses_node(6, (ast.If,)), (
        "Step 3: use an if statement to respond to the chosen action."
    )


def test_prints_a_response():
    run = run_student(6)
    assert run.output.strip(), "Step 3: print a response using the inputs."
