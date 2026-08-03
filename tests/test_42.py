"""Tests for Lesson 42: World Map and Locations."""
from _helpers import assert_scaffold_is_blank, defines_function, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(42)


def test_world_has_the_three_places():
    run = run_student(42)
    world = run.get("world")
    assert isinstance(world, dict), "Step 1: create a world map dictionary."
    keys = {str(k).lower() for k in world}
    for place in ("town", "forest", "cave"):
        assert place in keys, f"Step 1: the world needs a '{place}'."


def test_defines_the_helpers():
    assert defines_function(42, "show_location"), "Step 2: define show_location(place)."
    assert defines_function(42, "move"), "Step 3: define move(world, current, direction)."


def test_move_follows_the_map():
    run = run_student(42)
    world, move = run.get("world"), run.get("move")
    start = "town"
    exits = world[start] if isinstance(world[start], dict) else {}
    if exits:
        direction, destination = next(iter(exits.items()))
        assert move(world, start, direction) == destination, (
            "Step 3: move() should return the connected location."
        )


def test_move_rejects_a_bad_direction():
    run = run_student(42)
    world, move = run.get("world"), run.get("move")
    result = move(world, "town", "nowhere")
    assert result in (None, "town"), (
        "Step 3: an impossible direction should keep you put (return the "
        "current place or None), not crash."
    )
