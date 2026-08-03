"""
Lesson 31: The Hero Class - Your Adventure Begins
==================================================

WHAT YOU'LL LEARN
  How to build the Hero class that the rest of your game will use.
  From here on, every lesson adds a piece to one real game.

NEW WORDS
  class        A blueprint for a kind of thing. Hero describes what
               every hero in your game knows.
  __init__     The setup method. It runs automatically each time you
               create a hero, and gives it its starting values.
  self         Means "this particular hero". Always the first
               parameter of a method.
  attribute    A value stored on an object, reached with a dot:
               hero.health

HOW IT WORKS
  class Hero:
      def __init__(self, name):
          self.name = name
          self.health = 100
          self.gold = 50

  Only name is a parameter, because every new hero should begin with
  the same 100 health and 50 gold. Those are written straight into
  __init__ rather than being asked for.

      hero = Hero("Alex")
      print(hero.name, hero.health, hero.gold)

  Building a hero runs __init__ with self set to the new object, so
  all three attributes get filled in at once.

YOUR TASK
  Step 1: Create a class named Hero. Its __init__ must take self and
          name, then set:
            self.name    to the name that was passed in
            self.health  to 100
            self.gold    to 50
  Step 2: Create a Hero and print its name, health and gold.

EXAMPLE
  This example is a Robot, so you still write your own Hero.

      class Robot:
          def __init__(self, model):
              self.model = model
              self.battery = 100
              self.bolts = 50

      r = Robot("T-800")
      print(r.model, r.battery, r.bolts)

WHEN IT WORKS YOU'LL SEE
  Alex the hero has 100 health and 50 gold!

IF YOU GET STUCK
  AttributeError: no    -> you wrote health = 100 instead of
  attribute health         self.health = 100.
  TypeError: takes 1    -> __init__ needs self as its first
  positional argument      parameter, before name.
  health is not 100     -> do not make health a parameter. Set it to
                           100 inside __init__.

STYLE
  Class names use PascalCase (Hero), while variables and functions
  use snake_case (hero, add_item). Readers spot the difference
  instantly.

CHECK YOUR WORK
  python run_lesson.py 31
"""

# TODO: Write your code for Lesson 31 below this line.
