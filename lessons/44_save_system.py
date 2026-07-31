"""
Lesson 44: Save System
========================

Step 1: Create save_game(hero, location) -> savegame.json

Step 4: Test your code
  Run: python run_lesson.py 44
"""

import json

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.gold = 50
        self.location = "town"

def save_game(hero, location):
    """Save hero state to savegame.json."""
    save_data = {
        "name": hero.name,
        "health": hero.health,
        "gold": hero.gold,
        "location": location
    }
    with open("savegame.json", "w") as f:
        json.dump(save_data, f, indent=2)
