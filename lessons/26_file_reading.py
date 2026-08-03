r"""
Lesson 26: File Reading - Loading It Back
==========================================

WHAT YOU'LL LEARN
  How to read information back out of a file, so your game can
  remember things from last time.

NEW WORDS
  mode "r"      Read mode. Opens an existing file to look at it.
  .read()       Gives you the whole file as one long string.
  .readlines()  Gives you a list, with one string per line.
  .strip()      Removes spaces and the invisible newline character
                from the ends of a string.
  FileNotFoundError  The exception Python raises when the file is
                not there.

HOW IT WORKS
  with open("save.txt", "r") as f:
      lines = f.readlines()

  Now lines is a list like ["Musab\n", "120\n"]. Each string still
  carries the newline character that ended its line in the file, so
  you almost always clean it up:

      name = lines[0].strip()
      gold = lines[1].strip()

  Remember the list starts at index 0. If the numbers need to be used
  as numbers, convert them: int(gold).

  If the file might not exist yet, guard against it:

      try:
          with open("save.txt", "r") as f:
              ...
      except FileNotFoundError:
          print("No save file yet!")

YOUR TASK
  Step 1: Use with open("save.txt", "r") to open the file you made in
          Lesson 25 and read its lines.
  Step 2: Use .strip() to clean each line, then print the values you
          loaded.

EXAMPLE
  This example reads a shopping list, so you still write your own
  save loader.

      with open("shopping.txt", "r") as f:
          items = f.readlines()
      for item in items:
          print(item.strip())

WHEN IT WORKS YOU'LL SEE
  Loaded hero: Musab
  Loaded gold: 120

IF YOU GET STUCK
  FileNotFoundError    -> run Lesson 25 first so save.txt exists, or
                          catch the exception.
  Extra blank lines    -> you forgot .strip(), so the newline is
                          still attached.
  TypeError when       -> values read from a file are strings. Use
  adding                  int(...) before doing maths.

CHECK YOUR WORK
  python run_lesson.py 26
"""

# TODO: Write your code for Lesson 26 below this line.
