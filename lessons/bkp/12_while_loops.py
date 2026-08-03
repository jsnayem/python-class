"""
Lesson 12: Multiple Parameters
================================

Step 1: Write greet(name, greeting="Hello")

Step 2: Call with one arg and with both args

Step 4: Test your code
  Run: python run_lesson.py 12
"""

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alex")
greet("Mara", greeting="Hi")
