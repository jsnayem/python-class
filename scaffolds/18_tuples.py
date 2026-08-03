"""
Lesson 18: Tuples - Fixed Groups Of Values
===========================================

WHAT YOU'LL LEARN
  How to group a few values together in something that cannot be
  changed by accident, and how to pull the pieces back out.

NEW WORDS
  tuple        A collection written with round brackets:
               ("Sword", 25). Like a list, but frozen.
  immutable    Cannot be changed after it is made. Tuples are
               immutable; lists are not.
  index        The position of an item, counting from 0. The first
               item is weapon[0], the second is weapon[1].
  unpacking    Pulling a tuple apart into separate variables in one
               line: name, price = weapon

HOW IT WORKS
  weapon = ("Iron Sword", 25)

  This groups a name and a price into a single value. Read the parts
  back by index:

      print(weapon[0])
      print(weapon[1])

  Remember Python counts from 0, so index 0 is the name and index 1
  is the price. Because tuples are immutable, weapon[0] = "Axe" is an
  error. That is a feature: use a tuple when the values belong
  together and should not drift apart or be edited by mistake.

YOUR TASK
  Step 1: Create a tuple named weapon holding a weapon name and a
          number, in that order.
  Step 2: Print weapon[0] and print weapon[1].

EXAMPLE
  This example is about a map coordinate, so you still write your own
  weapon tuple.

      position = ("Forest", 7)
      print(position[0])
      print(position[1])

WHEN IT WORKS YOU'LL SEE
  Iron Sword
  25

IF YOU GET STUCK
  TypeError: does not     -> you tried to change a tuple. Make a new
  support item assignment    one instead, or use a list.
  IndexError: out of      -> you asked for weapon[2] but there are
  range                      only two items, at 0 and 1.
  Not actually a tuple    -> one value in brackets needs a trailing
                             comma: ("Sword",)

CHECK YOUR WORK
  python run_lesson.py 18
"""

# TODO: Write your code for Lesson 18 below this line.
