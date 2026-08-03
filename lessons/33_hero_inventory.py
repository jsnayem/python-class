"""
Lesson 33: Hero Inventory - Carrying Things
============================================

WHAT YOU'LL LEARN
  How to give every hero their own bag, and methods to put things in
  and take things out.

NEW WORDS
  inventory    The list of things a hero is carrying.
  .append()    Adds an item to the end of a list.
  .remove()    Takes the first matching item out of a list.
  per-object   Each hero needs their OWN list. Two heroes must never
               share one bag.

HOW IT WORKS
  class Hero:
      def __init__(self, name):
          self.name = name
          self.inventory = []

  Because self.inventory is created inside __init__, every hero gets
  a brand new empty list of their own. Now add the two methods:

      def add_item(self, item):
          self.inventory.append(item)

      def drop_item(self, item):
          self.inventory.remove(item)

  Using them looks like this:

      hero.add_item("sword")
      print(hero.inventory)      ->  ['sword']
      hero.drop_item("sword")
      print(hero.inventory)      ->  []

YOUR TASK
  Step 1: In Hero's __init__, add self.inventory and start it as an
          empty list.
  Step 2: Add a method named add_item that appends an item to the
          inventory, and a method named drop_item that removes one.
  Step 3: Create a hero, add an item, print the inventory, drop the
          item, and print it again.

EXAMPLE
  This example is a schoolbag, so you still write your own Hero
  methods.

      class Pupil:
          def __init__(self):
              self.bag = []

          def pack(self, thing):
              self.bag.append(thing)

      p = Pupil()
      p.pack("pencil")
      print(p.bag)

WHEN IT WORKS YOU'LL SEE
  Alex picks up a sword: ['sword']
  Alex drops the sword: []

IF YOU GET STUCK
  Both heroes share    -> you put inventory in the class body. It
  one bag                 must be self.inventory inside __init__.
  ValueError: list     -> .remove() needs an item that is actually
  .remove(x) not in       there. Add it before dropping it.
  list
  AttributeError       -> check the method names are exactly
                          add_item and drop_item.

CHECK YOUR WORK
  python run_lesson.py 33
"""

# TODO: Write your code for Lesson 33 below this line.
