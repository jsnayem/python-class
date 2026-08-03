"""
Lesson 45: The Load System - Continuing The Adventure
======================================================

WHAT YOU'LL LEARN
  How to read a save file back, and how to cope calmly when there
  is not one yet.

NEW WORDS
  load_game()  The function you will write. It reads the save file
               and gives the data back.
  json.load()  Reads JSON from an open file into a dictionary.
  FileNotFoundError  The exception raised when the file is missing.
  graceful     Handling a problem without crashing. A brand new
               player has no save file, and that is not an error.

HOW IT WORKS
  import json

  def load_game():
      try:
          with open("savegame.json", "r") as f:
              return json.load(f)
      except FileNotFoundError:
          return None

  The try block does the hopeful thing. If the file is missing,
  Python jumps to except and hands back None instead of crashing.

  Returning None is a deliberate signal meaning "there was nothing to
  load", so the code that called it can decide what to do:

      data = load_game()
      if data is None:
          print("No save found. Starting a new adventure!")
      else:
          print(f"Welcome back, {data['name']}!")

YOUR TASK
  Step 1: Import json, then define a function named load_game that
          takes no parameters, reads savegame.json with json.load()
          inside a try block, and returns the data.
  Step 2: Catch FileNotFoundError and return None when there is no
          save file yet.
  Step 3: Call load_game and print a different message depending on
          whether you got data back or None.

EXAMPLE
  This example loads settings, so you still write your own load_game.

      import json

      def load_settings():
          try:
              with open("settings.json", "r") as f:
                  return json.load(f)
          except FileNotFoundError:
              return None

WHEN IT WORKS YOU'LL SEE
  Welcome back, Alex! You have 50 gold and you are in the town.

  Or, when there is no save file:

  No save found. Starting a new adventure!

IF YOU GET STUCK
  It crashes with       -> the open() call must be inside the try
  FileNotFoundError        block, and except must name that error.
  It returns nothing    -> add return in front of json.load(f).
  JSONDecodeError       -> the save file is empty or damaged. Run
                           Lesson 44 again to rewrite it.

CHECK YOUR WORK
  python run_lesson.py 45
"""

# TODO: Write your code for Lesson 45 below this line.
