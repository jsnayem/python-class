"""Lesson 4: Math - Calculations
==============================
Step 1: Calculate damage = hero_attack - monster_defense
Step 2: Add 30 to hero_health
Step 3: Add monster_gold to hero_gold
Step 4: Test your code
  Run: python run_lesson.py 4
"""
hero_attack = 15
monster_defense = 7
damage = hero_attack - monster_defense
print(f"Damage dealt: {damage}")
hero_health = 100
hero_gold = 50
monster_gold = 20
hero_health = hero_health + 30
hero_gold = hero_gold + monster_gold
print(f"Health: {hero_health}, Gold: {hero_gold}")
