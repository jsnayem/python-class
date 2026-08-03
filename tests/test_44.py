"""Tests for Lesson 44: Save System."""
import json
import os
import tempfile

from _helpers import assert_scaffold_is_blank, defines_function, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(44)


def test_defines_save_game():
    assert defines_function(44, "save_game"), (
        "Step 1: define save_game(hero, location)."
    )


def _hero_like(run):
    Hero = run.get("Hero")
    if Hero is not None:
        return Hero("Zoe")

    class H:
        name = "Zoe"
        health = 70
        gold = 123
        inventory = []

    return H()


def test_save_game_writes_valid_json():
    run = run_student(44)
    hero = _hero_like(run)
    tmp = tempfile.mkdtemp()
    cwd = os.getcwd()
    try:
        os.chdir(tmp)
        run.get("save_game")(hero, "town")
        assert os.path.exists("savegame.json"), (
            "Step 1: save to a file called savegame.json."
        )
        data = json.load(open("savegame.json"))
    finally:
        os.chdir(cwd)
    assert isinstance(data, dict), "Step 1: save a dictionary of hero data."
    assert data.get("location") == "town", "Step 1: remember the location."
    assert str(hero.name) in json.dumps(data), "Step 1: remember the hero's name."
