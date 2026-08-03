"""
Lesson 31: Build the Hero Class
================================

Step 1: Create the Hero class with name, health, gold
Step 2: Create hero = Hero("Alex") and print stats
Step 3: Test your code
  Run: python run_lesson.py 31
"""

BASE_HEALTH = 100
BASE_GOLD = 50


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = BASE_HEALTH
        self.gold = BASE_GOLD
