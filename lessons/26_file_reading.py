"""
Lesson 26: File Reading
========================

Step 1: Open save.txt and read lines

Step 2: Print name and score

Step 4: Test your code
  Run: python run_lesson.py 26
"""
from pathlib import Path
p = Path("tests/tmp_save_25.txt")
if p.exists():
    with open(p, "r") as fh:
        data = fh.read().splitlines()
    print(f"Name: {data[0]}, Score: {data[1]}")
else:
    print("No save file")
