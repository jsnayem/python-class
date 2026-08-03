"""Tests for Lesson 43: Game Loop - Exploring."""
from _helpers import assert_scaffold_is_blank, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(43)


def test_world_map_exists():
    run = run_student(43)
    world = run.get("world")
    assert isinstance(world, dict) and world, "Step 1: create the world map."


def test_the_hero_moves_from_town_to_forest():
    run = run_student(43)
    location = run.get("current") or run.get("location") or run.get("current_location")
    assert location is not None, (
        "Step 3: keep the player's place in a variable called current (or "
        "location)."
    )
    assert str(location).lower() == "forest", (
        f"Step 3: after the deterministic move the player should be in the "
        f"forest, not {location!r}."
    )


def test_prints_the_journey():
    run = run_student(43)
    out = run.output.lower()
    assert "town" in out and "forest" in out, (
        "Step 3: print where the player is as they move."
    )
