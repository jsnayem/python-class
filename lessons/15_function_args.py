"""
Lesson 15: Dictionaries - Labelled Information
===============================================

WHAT YOU'LL LEARN
  How to store information under labels instead of positions, so you
  can look things up by name.

NEW WORDS
  dictionary   A collection that stores pairs of label and value,
               written with curly brackets: {"health": 100}.
  key          The label you look something up by, like "health".
  value        The information stored under that key, like 100.
  .keys()      A method giving back all the labels.
  .values()    A method giving back all the stored values.
  .items()     A method giving back both together, ideal for looping.

HOW IT WORKS
  hero_stats = {"name": "Alex", "health": 100, "gold": 50}

  A list would make you remember that position 1 is health. A
  dictionary lets you just ask for it by name:

      print(hero_stats["health"])

  To see everything, loop over .items(), which hands you the key and
  the value at the same time:

      for key, value in hero_stats.items():
          print(f"{key}: {value}")

YOUR TASK
  Step 1: Create a dictionary named hero_stats with the keys "name",
          "health" and "gold", and sensible values for each.
  Step 2: Print hero_stats.keys() and print hero_stats.values().
  Step 3: Loop over hero_stats.items() and print each key with its
          value on its own line.

EXAMPLE
  This example is about a bicycle, so you still write your own hero
  stats.

      bike = {"colour": "red", "gears": 18, "bell": True}
      print(bike.keys())
      print(bike.values())
      for key, value in bike.items():
          print(f"{key}: {value}")

WHEN IT WORKS YOU'LL SEE
  dict_keys(['name', 'health', 'gold'])
  dict_values(['Alex', 100, 50])
  name: Alex
  health: 100
  gold: 50

IF YOU GET STUCK
  KeyError            -> that key is not in the dictionary. Check
                         your spelling; keys are case sensitive.
  ValueError: too     -> looping over .items() needs two names:
  many values            for key, value in ...
  SyntaxError         -> dictionaries use curly brackets {} and a
                         colon between each key and its value.

CHECK YOUR WORK
  python run_lesson.py 15
"""

# TODO: Write your code for Lesson 15 below this line.
