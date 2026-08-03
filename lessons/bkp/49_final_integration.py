"""
Lesson 49: Final Integration
=============================

Step 1: print_header("GAME START")
Step 2: load_game()
Step 3: Create Hero and print welcome
Step 4: Test your code
  Run: python run_lesson.py 49
"""

import json
from typing import Optional

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.gold = 50

class Color:
    BRIGHT_YELLOW = "\033[93m"
    RESET = "\033[0m"

def print_header(title):
    """Print a decorative header."""
    border = "=" * 50
    print(f"\n{Color.BRIGHT_YELLOW}{border}{Color.RESET}")
    print(f"{Color.BRIGHT_YELLOW}{title.center(50)}{Color.RESET}")
    print(f"{Color.BRIGHT_YELLOW}{border}{Color.RESET}")

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

# Main game setup
print_header("GAME START")
hero = load_game()
if hero is None:
    name = input("Enter your hero's name: ").strip() or "Hero"
    hero = Hero(name)
print(f"Welcome, {hero.name}!")
