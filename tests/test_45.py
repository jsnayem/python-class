"""Tests for Lesson 45: Load System."""
import json
import os
import tempfile

from _helpers import assert_scaffold_is_blank, defines_function, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(45)


def test_defines_load_game():
    assert defines_function(45, "load_game"), "Step 1: define load_game()."


def test_load_game_reads_the_save_file():
    run = run_student(45)
    payload = {"name": "Zoe", "health": 70, "gold": 123, "location": "cave"}
    tmp = tempfile.mkdtemp()
    cwd = os.getcwd()
    try:
        os.chdir(tmp)
        with open("savegame.json", "w") as f:
            json.dump(payload, f)
        loaded = run.get("load_game")()
    finally:
        os.chdir(cwd)
    assert loaded is not None, "Step 1: return the data you loaded."
    text = json.dumps(loaded, default=str)
    assert "Zoe" in text and "123" in text, (
        "Step 1: the loaded data should contain what was in savegame.json."
    )


def test_load_game_returns_none_when_there_is_no_save():
    run = run_student(45)
    tmp = tempfile.mkdtemp()
    cwd = os.getcwd()
    try:
        os.chdir(tmp)
        assert run.get("load_game")() is None, (
            "Step 2: return None when savegame.json does not exist."
        )
    finally:
        os.chdir(cwd)
