"""Tests for Lesson 20: Object Interaction - Combat."""
from _helpers import assert_scaffold_is_blank, defines_class, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(20)


def test_defines_goblin_class():
    assert defines_class(20, "Goblin"), "Step 1: create the Goblin class."


def test_attacking_the_goblin_changes_it():
    run = run_student(20)
    Goblin = run.get("Goblin")
    goblin = Goblin()
    before = {k: v for k, v in vars(goblin).items() if isinstance(v, (int, float))}
    attack = run.get("attack") or getattr(goblin, "attack", None)
    assert callable(attack), "Step 2: create an attack function or method."
    try:
        attack(goblin)
    except TypeError:
        attack()
    after = {k: v for k, v in vars(goblin).items() if isinstance(v, (int, float))}
    assert before != after or run.output.strip(), (
        "Step 3: attacking should change the goblin (e.g. lower its health) "
        "or print the result."
    )


def test_prints_the_result():
    run = run_student(20)
    assert run.output.strip(), "Step 3: call attack and print the result."
