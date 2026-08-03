"""Tests for Lesson 17: Classes Introduction."""
from _helpers import assert_scaffold_is_blank, defines_class, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(17)


def test_defines_monster_class():
    assert defines_class(17, "Monster"), (
        "Step 1: create a class called Monster with __init__(self, name, hp)."
    )


def test_monster_stores_name_and_hp():
    run = run_student(17)
    monster = run.get("Monster")("Orc", 42)
    assert monster.name == "Orc", "Step 1: store the name on self.name."
    assert monster.hp == 42, "Step 1: store the hp on self.hp."


def test_creates_and_prints_a_goblin():
    run = run_student(17)
    goblin = run.get("goblin")
    assert goblin is not None, 'Step 2: create goblin = Monster("Goblin", 30).'
    assert goblin.name == "Goblin" and goblin.hp == 30
    assert "goblin" in run.output.lower(), "Step 3: print goblin.name."
    assert "30" in run.output, "Step 3: print goblin.hp."
