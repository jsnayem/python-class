"""
Lesson 35: Weapon Class
========================

Step 1: Create Item(base)
Step 2: Create Weapon(Item) and Potion(Item)
Step 3: Create both and print them
Step 4: Test your code
  Run: python run_lesson.py 35
"""

class Item:
    def __init__(self, name, description, value):
        pass

class Weapon(Item):
    def __init__(self, name, description, value, attack_bonus):
        pass

class Potion(Item):
    def __init__(self, name, description, value, heal_amount):
        pass
