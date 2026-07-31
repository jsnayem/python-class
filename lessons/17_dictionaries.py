"""
Lesson 17: Classes Introduction
=================================

Step 1: Create class Monster with __init__(self, name, hp)

Step 2: Create goblin = Monster("Goblin", 30)

Step 3: Print goblin.name and goblin.hp

Step 4: Test your code
  Run: python run_lesson.py 17
"""

class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

goblin = Monster("Goblin", 30)
print(f"{goblin.name} has {goblin.hp} HP")
