"""
Lesson 42: The World Map - Places And Paths
============================================

WHAT YOU'LL LEARN
  How to describe a whole world as a dictionary of places, each
  knowing which way leads where.

NEW WORDS
  world        A dictionary where each key is a place name and each
               value describes that place.
  nested       A dictionary inside another dictionary. Your exits
               live nested inside each place.
  exits        The directions you can travel from a place, and where
               each one leads.
  .get()       Looks a key up but returns None instead of crashing
               when it is missing.

HOW IT WORKS
  world = {
      "town":   {"north": "forest", "east": "cave"},
      "forest": {"south": "town"},
      "cave":   {"west": "town"},
  }

  Each place maps a direction to the place it leads to. So from town,
  north leads to forest. Now two helper functions:

      def show_location(place):
          print(f"You are in the {place}.")

      def move(world, current, direction):
          return world[current].get(direction)

  world[current] gives the exits for where you are. Using .get() on
  it means an impossible direction returns None instead of crashing,
  so your game can politely say "you cannot go that way."

YOUR TASK
  Step 1: Create a dictionary named world containing at least the
          places "town", "forest" and "cave", each holding its own
          dictionary of directions to other places.
  Step 2: Define a function named show_location that takes place and
          prints where the hero is.
  Step 3: Define a function named move that takes world, current and
          direction, and returns the place that direction leads to,
          or None when there is no path that way.

EXAMPLE
  This example is a house, so you still write your own world.

      house = {
          "hall":    {"up": "landing"},
          "landing": {"down": "hall"},
      }

      def go(house, room, direction):
          return house[room].get(direction)

      print(go(house, "hall", "up"))
      print(go(house, "hall", "left"))

WHEN IT WORKS YOU'LL SEE
  You are in the town.
  You travel north...
  You are in the forest.
  You cannot go that way.

IF YOU GET STUCK
  KeyError              -> use .get(direction) instead of
                           [direction] so missing paths return None.
  TypeError: string     -> each place's value must be a dictionary
  indices                  of directions, not a plain string.
  move returns None     -> check the direction spelling matches a key
  always                   in that place's exits.

CHECK YOUR WORK
  python run_lesson.py 42
"""

# TODO: Write your code for Lesson 42 below this line.
