"""
Lesson 44: The Save System - Remembering Progress
==================================================

WHAT YOU'LL LEARN
  How to write the hero's progress into a file, so the adventure
  survives closing the program.

NEW WORDS
  save_game()  The function you will write. It takes the hero and
               their location and writes them to disk.
  savegame.json  The file your game saves into.
  json.dump()  Writes a dictionary into an open file as JSON.
  serialise    To turn objects into plain data (numbers, strings,
               lists, dictionaries) that a file can hold.

HOW IT WORKS
  import json

  def save_game(hero, location):
      data = {
          "name": hero.name,
          "health": hero.health,
          "gold": hero.gold,
          "location": location,
      }
      with open("savegame.json", "w") as f:
          json.dump(data, f)

  You cannot write a Hero object straight into a file. Instead you
  build a dictionary of its plain values first: that is serialising.
  The key "location" matters, because loading needs to know where the
  hero was standing.

  Using json means loading it back gives you real numbers again,
  rather than strings you must convert by hand.

YOUR TASK
  Step 1: Import json, then define a function named save_game that
          takes hero and location, builds a dictionary containing the
          hero's name, health and gold plus a "location" key, and
          writes it to savegame.json with json.dump().
  Step 2: Create a Hero, call save_game with it, and print a message
          confirming the game was saved.

EXAMPLE
  This example saves a quiz result, so you still write your own
  save_game.

      import json

      def save_score(player, level):
          data = {"name": player.name, "score": player.score,
                  "level": level}
          with open("score.json", "w") as f:
              json.dump(data, f)

WHEN IT WORKS YOU'LL SEE
  Game saved! Alex is resting in the town with 50 gold.

IF YOU GET STUCK
  TypeError: Object of  -> you tried to save the Hero object itself.
  type Hero is not         Build a dictionary of its values first.
  JSON serializable
  No file appears       -> check you called save_game(...), not just
                           defined it.
  KeyError on loading   -> make sure you included the "location" key.

STYLE
  Reuse what you already wrote. save_game builds on the Hero class
  from Lesson 31 and the json skills from Lesson 27 rather than
  starting again. Not repeating yourself is what DRY means.

CHECK YOUR WORK
  python run_lesson.py 44
"""

# TODO: Write your code for Lesson 44 below this line.
