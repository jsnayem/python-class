"""
Lesson 28: Random - Making The Game Unpredictable
==================================================

WHAT YOU'LL LEARN
  How to roll dice in code, so battles are exciting instead of
  identical every single time.

NEW WORDS
  random          A module of functions that produce unpredictable
                  results.
  random.randint(1, 6)  Gives a whole number from 1 to 6. Unlike
                  range(), both ends are included.
  random.choice() Picks one item out of a list at random.
  simulate        To model something in code, like rolling dice or
                  fighting several rounds.

HOW IT WORKS
  import random

  def roll_dice(sides=6):
      return random.randint(1, sides)

  random.randint(1, sides) gives a whole number from 1 up to and
  including sides. Because sides has a default of 6, roll_dice()
  rolls an ordinary six-sided die, while roll_dice(20) rolls a
  twenty-sided one.

      loot_table = ["Gold Coin", "Rusty Sword", "Health Potion"]

      def random_loot():
          return random.choice(loot_table)

  random.choice() picks one element out of a list. Returning it means
  the caller can print it or add it to an inventory.

YOUR TASK
  Step 1: Import random, then define a function named roll_dice with
          one optional parameter named sides whose default is 6. It
          must return a number from 1 to sides.
  Step 2: Call roll_dice() and print the result, then call
          roll_dice(20) to show a bigger die.
  Step 3: Create a list of loot items, then define a function named
          random_loot that returns one of them at random.
  Step 4: Use a loop to roll three times and print what you find.

EXAMPLE
  This example picks a lunch, so you still write your own dice and
  loot.

      import random

      lunches = ["pizza", "pasta", "curry"]

      def random_lunch():
          return random.choice(lunches)

      def spin(sides=3):
          return random.randint(1, sides)

      print(random_lunch())
      print(spin())

WHEN IT WORKS YOU'LL SEE
  You roll a 4 on a six-sided die.
  You roll a 17 on a twenty-sided die.
  You find: Health Potion
  You find: Gold Coin
  You find: Health Potion

  (Your numbers change every run. That is the point.)

IF YOU GET STUCK
  NameError: random     -> add import random at the top.
  Same number always    -> call roll_dice() inside the loop, not once
                           before it.
  roll_dice() gives an  -> randint(1, sides) includes both ends,
  unexpected number        unlike range().
  TypeError: missing    -> sides needs a default:
  argument                 def roll_dice(sides=6)

CHECK YOUR WORK
  python run_lesson.py 28
"""

# TODO: Write your code for Lesson 28 below this line.
