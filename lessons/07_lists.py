"""
Lesson 7: Lists - Holding Many Things
======================================

WHAT YOU'LL LEARN
  How to keep lots of values in one variable, add to it, and show
  every item with a number beside it.

NEW WORDS
  list         A variable that holds many values in order, written
               with square brackets: ["sword", "shield"].
  element      One single item inside a list.
  index        The position of an element. Python counts from 0, so
               the first element is at index 0, not 1.
  .append()    A list method that adds one new element to the end.
  enumerate()  A built-in that walks a list and hands you both the
               position number and the element at the same time.

HOW IT WORKS
  inventory = []

  Empty square brackets make an empty list, ready to be filled.

      inventory.append("Health Potion")

  .append() adds one item onto the end. Do this twice and the list
  holds two items, in the order you added them.

      for position, item in enumerate(inventory, start=1):
          print(f"{position}. {item}")

  enumerate() gives you two things each time round the loop: the
  number and the item. start=1 makes it count 1, 2, 3 for humans
  instead of 0, 1, 2.

YOUR TASK
  Step 1: Create an empty list named inventory.
  Step 2: Use .append() to add "Health Potion" and then "Iron Sword".
  Step 3: Print every item with a number next to it, so the player
          can see a numbered bag.

EXAMPLE
  This example is about a lunchbox, so you still write your own
  inventory.

      lunchbox = []
      lunchbox.append("Sandwich")
      lunchbox.append("Apple")
      for position, food in enumerate(lunchbox, start=1):
          print(f"{position}. {food}")

WHEN IT WORKS YOU'LL SEE
  1. Health Potion
  2. Iron Sword

IF YOU GET STUCK
  AttributeError        -> .append() only works on lists. Check you
                           made inventory with square brackets.
  Only the last item    -> you replaced the list instead of appending
  shows                    to it. Use inventory.append(...) each time.
  Numbers start at 0    -> add start=1 inside enumerate().

CHECK YOUR WORK
  python run_lesson.py 7
"""

# TODO: Write your code for Lesson 7 below this line.
