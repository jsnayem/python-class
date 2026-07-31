"""Lesson 6: Input
================
Step 1: Ask for hero name using input()
Step 2: Ask for action choice using input()
Step 3: Print a response using the inputs
Step 4: Test your code
  Run: python run_lesson.py 6
"""
hero_name = input("Enter your hero's name: ")
action = input("Enter your action (a/f): ")
if action in ("a", "f"):
    print(f"{hero_name} chooses to {action}")
else:
    print(f"{hero_name} chose an invalid action: {action}")
