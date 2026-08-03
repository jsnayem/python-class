"""
Lesson 25: File Writing
========================

Step 1: Write player_name and player_gold to save.txt

Step 3: Test your code
  Run: python run_lesson.py 25
"""
from pathlib import Path
player_name = "Alex"
player_gold = 120
out = Path("tests/tmp_save_25.txt")
with open(out, "w") as fh:
    fh.write(f"{player_name}\n{player_gold}\n")
assert out.exists()
