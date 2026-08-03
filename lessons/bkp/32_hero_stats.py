"""
Lesson 32: Hero Stats - Starting Bonuses
==========================================

Step 1: Add max_health in __init__
Step 2: Add is_alive() method
Step 3: Test alive and dead states
Step 4: Test your code
  Run: python run_lesson.py 32
"""

BASE_HEALTH = 100
BASE_GOLD = 50


class Hero:
    def __init__(self, name):
        self.name = name
        self.max_health = BASE_HEALTH
        self.health = self.max_health
        self.gold = BASE_GOLD

    def is_alive(self):
        return self.health > 0
