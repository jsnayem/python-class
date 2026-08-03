"""
Lesson 27: JSON - Saving Whole Structures
==========================================

WHAT YOU'LL LEARN
  How to save an entire dictionary to a file in one go, and load it
  back exactly as it was, without cleaning up strings by hand.

NEW WORDS
  module        A ready-made bundle of code you can borrow.
  import        The keyword that brings a module into your program.
  JSON          A standard text format for storing structured data.
                Nearly every program in the world understands it.
  json.dump()   Writes a Python dictionary into an open file.
  json.load()   Reads it back out again as a real dictionary.

HOW IT WORKS
  import json

  Put the import line at the very top of your file. Then saving a
  whole dictionary takes one line:

      hero = {"name": "Musab", "health": 100, "gold": 120}
      with open("hero.json", "w") as f:
          json.dump(hero, f)

  Loading it back gives you a real dictionary again, with the numbers
  still numbers:

      with open("hero.json", "r") as f:
          loaded = json.load(f)
      print(loaded["name"])

  Compare that with Lesson 26, where every value came back as a
  string you had to strip and convert. This is why real programs use
  JSON for save files.

YOUR TASK
  Step 1: Import the json module at the top of your file.
  Step 2: Create a dictionary describing your hero, then use
          json.dump() to save it into hero.json.
  Step 3: Use json.load() to read the file back, and print a value
          from the loaded dictionary.

EXAMPLE
  This example saves settings, so you still write your own hero save.

      import json

      settings = {"volume": 7, "difficulty": "easy"}
      with open("settings.json", "w") as f:
          json.dump(settings, f)

      with open("settings.json", "r") as f:
          back = json.load(f)
      print(back["difficulty"])

WHEN IT WORKS YOU'LL SEE
  Saved hero to hero.json
  Loaded hero: Musab with 120 gold

IF YOU GET STUCK
  NameError: json is    -> add import json at the top of the file.
  not defined
  Argument order        -> it is json.dump(data, file), data first.
  JSONDecodeError       -> the file is empty or damaged. Save it
                           again before loading.

CHECK YOUR WORK
  python run_lesson.py 27
"""

# TODO: Write your code for Lesson 27 below this line.
