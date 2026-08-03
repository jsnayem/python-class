"""
Lesson 23: super() - Letting The Parent Do Its Job
===================================================

WHAT YOU'LL LEARN
  How a subclass can add its own information while still letting the
  parent class set up everything it already knows how to set up.

NEW WORDS
  super()      A built-in that means "the parent class". You use it
               to call the parent's version of a method.
  super().__init__(...)  Runs the parent's setup code from inside the
               child's own __init__.
  price        The name this lesson uses for how much an item costs.
  bonus        The extra attack a Weapon adds.
  amount       How much health a Potion restores.

HOW IT WORKS
  class Item:
      def __init__(self, name, price):
          self.name = name
          self.price = price

  A Weapon needs a name and price like any item, plus a bonus. Rather
  than repeating the two lines, it asks its parent to do them:

      class Weapon(Item):
          def __init__(self, name, price, bonus):
              super().__init__(name, price)
              self.bonus = bonus

  The super() line runs Item's __init__, which sets self.name and
  self.price. Then the child sets the one extra thing it cares about.

      sword = Weapon("Sword", 50, 5)
      print(sword.name, sword.price, sword.bonus)

  Forget the super() line and name and price never get set at all.

YOUR TASK
  Step 1: Create a base class named Item whose __init__ takes self,
          name and price. Then create two subclasses of it: Weapon
          and Potion.
  Step 2: In each subclass __init__, call super().__init__(...) first,
          then store the extra value: bonus for Weapon, amount for
          Potion.
  Step 3: Create one Weapon and one Potion, and print both.

EXAMPLE
  This example is about staff at a shop, so you still write your own
  Item, Weapon and Potion.

      class Person:
          def __init__(self, name):
              self.name = name

      class Cashier(Person):
          def __init__(self, name, till):
              super().__init__(name)
              self.till = till

      c = Cashier("Ada", 3)
      print(c.name, c.till)

WHEN IT WORKS YOU'LL SEE
  Sword costs 50 gold (+5 attack)
  Health Potion costs 20 gold (heals 30)

IF YOU GET STUCK
  AttributeError: no    -> you forgot the super().__init__ line, so
  attribute name           the parent never stored it.
  TypeError: missing    -> pass the parent exactly the arguments its
  argument                 own __init__ expects.
  Order matters         -> call super().__init__ first, then set your
                           extra attributes.

CHECK YOUR WORK
  python run_lesson.py 23
"""

# TODO: Write your code for Lesson 23 below this line.
