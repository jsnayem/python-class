"""Reference solution: Lesson 19 - Multiple Classes.

Demonstrates a base class (Animal) and a subclass (Dog) using inheritance.
The answer_key/ directory holds canonical teacher reference solutions; the
per-lesson tests in tests/ check the student's own lessons/ submissions.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self) -> str:
        return "..."


class Dog(Animal):
    def speak(self):
        return "Woof!"
