"""Lesson 10: Functions
=====================
Step 1: Define show_status(name, health, gold)
Step 2: Call it for two different heroes
Step 3: Define calculate_damage(base, bonus): return ...
Step 4: Test your code
  Run: python run_lesson.py 10
"""
def show_status(name, health, gold):
    print(f"{name}: HP {health}, Gold {gold}")
show_status("Alex", 100, 50)
show_status("Mara", 80, 75)
def calculate_damage(base, bonus):
    return base + bonus
damage = calculate_damage(10, 5)
print(f"Damage dealt: {damage}")
