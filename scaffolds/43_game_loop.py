"""
Lesson 43: The Game Loop - Actually Travelling
===============================================

WHAT YOU'LL LEARN
  How to keep track of where the hero is right now, and update that
  as they walk around the world you built.

NEW WORDS
  current      The variable holding the hero's location at this
               moment. This lesson uses the name current.
  game loop    The repeating heart of a game: show the situation,
               take an action, update the state, repeat.
  state        Information that changes as the game runs. The hero's
               location is state.
  update       To replace the old value with the new one, as in
               current = move(world, current, "north")

HOW IT WORKS
  world = {
      "town":   {"north": "forest"},
      "forest": {"south": "town"},
  }
  current = "town"

  The variable current remembers where the hero is. Travelling means
  working out the new place and storing it back:

      print(f"You are in the {current}.")
      current = move(world, current, "north")
      print(f"You are now in the {current}.")

  That reassignment is the whole idea. If you call move() but do not
  store the answer, the hero never actually goes anywhere. After
  moving north from town, current holds "forest".

YOUR TASK
  Step 1: Create your world dictionary again, with town connected to
          forest.
  Step 2: Create a variable named current holding the hero's starting
          location, "town".
  Step 3: Move the hero north and store the result back in current,
          so current ends up holding "forest".
  Step 4: Print where the hero is before and after the journey, so
          both town and forest appear on screen.

EXAMPLE
  This example is a board game counter, so you still write your own
  travelling hero.

      squares = {"start": {"forward": "middle"}}
      position = "start"
      print(f"On {position}")
      position = squares[position]["forward"]
      print(f"Now on {position}")

WHEN IT WORKS YOU'LL SEE
  You are in the town.
  You travel north through the trees...
  You are now in the forest.

IF YOU GET STUCK
  current never        -> you called move() without storing it. Write
  changes                 current = move(...)
  KeyError             -> the direction must exist in that place's
                          exits.
  The test cannot      -> name the variable exactly current.
  find your location

CHECK YOUR WORK
  python run_lesson.py 43
"""

# TODO: Write your code for Lesson 43 below this line.
