"""
Lesson 34: The Item Class - Things Worth Having
================================================

WHAT YOU'LL LEARN
  How to build the Item class, the base that every treasure, weapon
  and potion in your game will be built from.

NEW WORDS
  base class   A general class that more specific ones will build on
               later. Item is the base for Weapon and Potion.
  description  A short piece of text saying what the item is.
  value        How much gold the item is worth.

HOW IT WORKS
  class Item:
      def __init__(self, name, description, value):
          self.name = name
          self.description = description
          self.value = value

  All three are parameters this time, because every item is
  different. Compare that with Hero, where health was always 100.

      ring = Item("Ring", "A shiny ring", 25)
      print(f"{ring.name}: {ring.description} ({ring.value} gold)")

  Keep the parameter order in mind: name first, then description,
  then value. Later lessons build Weapon and Potion on top of this
  exact order.

YOUR TASK
  Step 1: Create a class named Item whose __init__ takes self, name,
          description and value, and stores all three on self.
  Step 2: Create an Item and print its name, description and value.

EXAMPLE
  This example is a museum exhibit, so you still write your own Item.

      class Exhibit:
          def __init__(self, title, info, year):
              self.title = title
              self.info = info
              self.year = year

      e = Exhibit("Vase", "A very old pot", 1801)
      print(e.title, e.info, e.year)

WHEN IT WORKS YOU'LL SEE
  Ring: A shiny ring (25 gold)

IF YOU GET STUCK
  TypeError: missing    -> Item needs all three arguments:
  2 required arguments     Item("Ring", "A shiny ring", 25)
  Values in the wrong   -> the order is name, description, value.
  places
  AttributeError        -> every one must be stored with self.

CHECK YOUR WORK
  python run_lesson.py 34
"""

# TODO: Write your code for Lesson 34 below this line.
