"""
Lesson 22: Inheritance - A Weapon Is An Item
=============================================

WHAT YOU'LL LEARN
  How to design a general class and then a more specific version of
  it, which is how real programs organise related things.

NEW WORDS
  base class   The general class other classes build on. Here, Item.
  subclass     The more specific class. Here, Weapon is a subclass
               of Item, because every weapon IS an item.
  is-a         The test for whether inheritance is right. A Weapon
               is-a Item, so Weapon(Item) makes sense.

HOW IT WORKS
  class Item:
      def __init__(self, name, value):
          self.name = name
          self.value = value

  Every item in your game has a name and a value. A weapon has those
  too, plus something extra, so it subclasses Item:

      class Weapon(Item):
          pass

  Even with pass (which means "nothing extra yet"), Weapon already
  has __init__, name and value, all inherited:

      sword = Weapon("Iron Sword", 25)
      print(sword.name, sword.value)

  Python can confirm the relationship for you:

      print(isinstance(sword, Item))    ->  True

  A Weapon really is an Item, so anything that works with Items works
  with Weapons too.

YOUR TASK
  Step 1: Create a base class named Item whose __init__ takes self,
          name and value, and stores both.
  Step 2: Create a subclass named Weapon by writing class
          Weapon(Item).
  Step 3: Create a Weapon and print its name and value.

EXAMPLE
  This example is about furniture, so you still write your own Item
  and Weapon.

      class Furniture:
          def __init__(self, name, price):
              self.name = name
              self.price = price

      class Chair(Furniture):
          pass

      seat = Chair("Oak Chair", 40)
      print(seat.name, seat.price)

WHEN IT WORKS YOU'LL SEE
  Iron Sword is worth 25 gold

IF YOU GET STUCK
  NameError: Item is    -> define Item above Weapon in the file.
  not defined
  SyntaxError           -> an empty class body needs the word pass.
  TypeError on          -> Weapon takes whatever Item's __init__
  Weapon(...)              takes, unless you write your own.

CHECK YOUR WORK
  python run_lesson.py 22
"""

# TODO: Write your code for Lesson 22 below this line.
