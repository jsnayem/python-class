"""
Lesson 45: Load System
========================

Step 1: Write load_game() reading savegame.json
Step 2: Return None if missing
Step 4: Test your code
  Run: python run_lesson.py 45
"""

import json
from typing import Optional

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.gold = 50

def load_game() -> Optional[Hero]:
    """Load hero from savegame.json. Returns None if file missing."""
    try:
        with open("savegame.json", "r") as f:
            data = json.load(f)
        hero = Hero(data["name"])
        hero.health = data.get("health", 100)
        hero.gold = data.get("gold", 50)
        return hero
    except FileNotFoundError:
        return None
