"""Tests for Lesson 2: Variables."""
from _helpers import assert_scaffold_is_blank, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(2)


def test_variables_exist_with_required_values():
    run = run_student(2)
    for name in ("hero_name", "hero_health", "hero_gold"):
        assert name in run, f"Step 1: create a variable called {name}."
    assert isinstance(run.get("hero_name"), str), "hero_name should be a string."
    assert run.get("hero_health") == 100, "Step 1: hero_health should be 100."


def test_gold_increases_by_twenty():
    # Behavioural: any correct form works (+= , = x + 20, = 20 + x ...).
    run = run_student(2)
    assert run.get("hero_gold") == 70, (
        f"Step 3: hero_gold should be 70 (50 starting gold + 20), got "
        f"{run.get('hero_gold')!r}."
    )


def test_prints_the_values_with_an_f_string():
    run = run_student(2)
    assert str(run.get("hero_name")) in run.output, (
        "Step 2: print your hero's name."
    )
    assert "100" in run.output and "70" in run.output, (
        "Step 2/3: print the health and the new gold total."
    )
