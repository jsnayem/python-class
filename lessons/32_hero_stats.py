"""
Lesson 32: Hero Stats - Maximum Health And Staying Alive
=========================================================

WHAT YOU'LL LEARN
  How to remember a hero's full health as well as their current
  health, and how to write a method that answers a yes-or-no
  question.

NEW WORDS
  max_health   The most health this hero can ever have. Current
               health goes up and down; max_health does not.
  method       A function defined inside a class. Its first
               parameter is always self.
  boolean      A True or False value.
  is_alive()   The method you will write. Methods that answer a
               question are usually named starting with is_ or has_.

HOW IT WORKS
  class Hero:
      def __init__(self, name):
          self.name = name
          self.max_health = 100
          self.health = self.max_health

  Setting health from max_health means a new hero starts completely
  full, and you only have the number 100 written once.

      def is_alive(self):
          return self.health > 0

  self.health > 0 is a comparison, so it is already True or False.
  Returning it directly is neater than an if statement. Now the rest
  of your game can simply ask:

      if hero.is_alive():
          print("Still fighting!")

YOUR TASK
  Step 1: In Hero's __init__, add self.max_health set to 100, and set
          self.health to the same value so a new hero starts full.
  Step 2: Add a method named is_alive that returns True while health
          is above 0, and False otherwise.
  Step 3: Print the alive state, then set the hero's health to 0 and
          print it again, to show both cases.

EXAMPLE
  This example is a torch, so you still write your own Hero.

      class Torch:
          def __init__(self):
              self.max_fuel = 60
              self.fuel = self.max_fuel

          def is_lit(self):
              return self.fuel > 0

      t = Torch()
      print(t.is_lit())
      t.fuel = 0
      print(t.is_lit())

WHEN IT WORKS YOU'LL SEE
  Alex is alive: True
  After a terrible blow, alive: False

IF YOU GET STUCK
  is_alive gives None   -> you forgot the word return.
  It returns 0 or 100   -> return self.health > 0, not self.health.
  AttributeError:       -> add self.max_health inside __init__.
  max_health

CHECK YOUR WORK
  python run_lesson.py 32
"""

# TODO: Write your code for Lesson 32 below this line.
