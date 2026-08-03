"""Tests for Lesson 21: Class Attributes."""
from _helpers import assert_scaffold_is_blank, defines_class, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(21)


def test_defines_hero_with_a_class_attribute():
    assert defines_class(21, "Hero"), "Step 1: create the Hero class."
    run = run_student(21)
    Hero = run.get("Hero")
    assert hasattr(Hero, "class_item"), (
        "Step 1: add a class attribute called class_item to Hero."
    )


def test_class_attribute_is_shared_by_instances():
    run = run_student(21)
    Hero = run.get("Hero")
    hero = Hero("Alex") if _takes_name(Hero) else Hero()
    assert hero.class_item == Hero.class_item, (
        "Step 2: the same class_item should be reachable via self and via the "
        "class itself."
    )


def _takes_name(cls):
    import inspect

    try:
        return len(inspect.signature(cls.__init__).parameters) > 1
    except (TypeError, ValueError):
        return False


def test_prints_the_class_item():
    run = run_student(21)
    item = str(run.get("Hero").class_item)
    assert item.lower() in run.output.lower(), "Step 2: print the class_item."
