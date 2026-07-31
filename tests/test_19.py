"""Tests for Lesson 19: Multiple Classes (inheritance).

Imports the teacher reference solution from answer_key/ and checks real
behavior (not just the word "class"). The student's own work lives in
lessons/ and is validated by the keyword check below.
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).parent.parent


def _load_answer(modname):
    spec = importlib.util.spec_from_file_location(
        modname, ROOT / "answer_key" / f"{modname}.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_student_file_present():
    lesson_files = sorted((ROOT / "lessons").glob("19_*.py"))
    assert lesson_files, "Lesson 19 file should exist"


def test_student_has_class_keywords():
    text = (ROOT / "lessons" / next((ROOT / "lessons").glob("19_*.py")).name).read_text()
    assert "class Animal" in text and "class Dog" in text


def test_answer_animal_holds_name():
    m = _load_answer("19_classes_intro")
    a = m.Animal("Rex")
    assert a.name == "Rex"


def test_answer_dog_is_animal():
    m = _load_answer("19_classes_intro")
    d = m.Dog("Buddy")
    assert isinstance(d, m.Animal)
    assert d.name == "Buddy"
    assert d.speak() == "Woof!"
