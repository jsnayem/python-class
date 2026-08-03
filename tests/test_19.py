"""Tests for Lesson 19: Multiple Classes (inheritance).

Student grading runs the student's own file. The ``test_reference_*`` cases
document the intended behaviour using answer_key/ and are for the teacher.
"""
from _helpers import assert_scaffold_is_blank, load_answer, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(19)


def test_animal_holds_a_name():
    run = run_student(19)
    Animal = run.get("Animal")
    assert Animal is not None, "Step 1: create the Animal class."
    assert Animal("Rex").name == "Rex", "Step 1: Animal should store self.name."


def test_dog_inherits_from_animal():
    run = run_student(19)
    Animal, Dog = run.get("Animal"), run.get("Dog")
    assert Dog is not None, "Step 2: create the Dog class."
    dog = Dog("Buddy")
    assert isinstance(dog, Animal), "Step 2: Dog should inherit from Animal."
    assert dog.name == "Buddy", "Step 2: Dog should keep the name."


def test_prints_dog_info():
    run = run_student(19)
    assert run.output.strip(), "Step 3: print information about your dog."


def test_reference_dog_speaks():
    m = load_answer("19_inheritance_intro")
    assert m.Dog("Buddy").speak() == "Woof!"
