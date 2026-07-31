"""
Lesson 23: Inheritance - Shop Items
======================================

Step 1: Define Item(base), Weapon(Item), Potion(Item)
Step 2: Each child calls super().__init__
Step 3: Create 1 Weapon and 1 Potion, print both
Step 4: Test your code
  Run: python run_lesson.py 23
"""

class Item:
    def __init__(self, name, price):
        pass

class Weapon(Item):
    def __init__(self, name, price, bonus):
        pass

class Potion(Item):
    def __init__(self, name, price, amount):
        pass
