"""Lesson 7: Lists
================
Step 1: Create an empty inventory list
Step 2: Append "Health Potion" and "Iron Sword"
Step 3: Print each item with a number using enumerate()
Step 4: Test your code
  Run: python run_lesson.py 7
"""
inventory = []
inventory.append("Health Potion")
inventory.append("Iron Sword")
for idx, item in enumerate(inventory, 1):
    print(f"{idx}. {item}")
