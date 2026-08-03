"""Reference solution: Lesson 40 - Flee Mechanic.

Returns True if the hero escapes, based on a probability chance (default 50%).
"""

import random


def flee(chance=0.5):
    return random.random() < chance


if __name__ == "__main__":
    print("You try to escape...")
    print("You got away!" if flee() else "The monster blocks your path!")
