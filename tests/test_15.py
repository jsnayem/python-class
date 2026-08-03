"""Tests for Lesson 15: Dictionary Methods."""
from _helpers import assert_scaffold_is_blank, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(15)


def test_hero_stats_dictionary_exists():
    run = run_student(15)
    stats = run.get("hero_stats")
    assert isinstance(stats, dict), "Step 1: create the hero_stats dictionary."
    for key in ("name", "health", "gold"):
        assert key in stats, f"Step 1: hero_stats needs a '{key}' key."


def test_prints_keys_and_values():
    run = run_student(15)
    stats = run.get("hero_stats", {})
    out = run.output.lower()
    for key in stats:
        assert str(key).lower() in out, f"Step 2: print the key '{key}'."
    for value in stats.values():
        assert str(value).lower() in out, f"Step 2: print the value '{value}'."
