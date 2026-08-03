"""
Lesson 30: F-Strings and Formatting
======================================

Step 1: Create hero, hp, gold variables

Step 2: Print an aligned status table

Step 4: Test your code
  Run: python run_lesson.py 30
"""
hero = "Alex"
hp = 95
gold = 210
print(f"{hero:10} | HP {hp:3} | Gold {gold:4}")
assert f"HP {hp}" in f"{hero:10} | HP {hp:3} | Gold {gold:4}"
