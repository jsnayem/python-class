"""
Lesson 20: Object Interaction - Combat
========================================

Step 1: Create Goblin class
Step 2: Create attack(goblin) method
Step 3: Call attack and print result
Step 4: Test your code
  Run: python run_lesson.py 20
"""


class Goblin:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


def attack(goblin):
    print(f"Attacked {goblin.name}! HP={goblin.hp}")


goblin = Goblin("Snag", 18)
attack(goblin)
