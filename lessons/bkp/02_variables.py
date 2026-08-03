"""Lesson 2: Variables - Storing Information
==========================================
In this lesson you'll create variables for your hero and print them.
Step 1: Create variables
  - hero_name = your hero's name (a string)
  - hero_health = 100
  - hero_gold = 50
Step 2: Print the variables using f-strings
Step 3: Add 20 to hero_gold and print the new total
Step 4: Test your code
  Run: python run_lesson.py 2
"""
hero_name = "Alex"
hero_health = 100
hero_gold = 50
print(f"Hero name: {hero_name}")
print(f"Hero health: {hero_health}")
print(f"Hero gold: {hero_gold}")
hero_gold = hero_gold + 20
print(f"Gold after finding treasure: {hero_gold}")
