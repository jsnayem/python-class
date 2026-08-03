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

  roll = random.randint(1, 20)
  print(f"You rolled {roll}")

  Every time you run this you may get a different number between 1
  and 20, including both 1 and 20 themselves.

      monsters = ["Goblin", "Orc", "Slime"]
      enemy = random.choice(monsters)

  random.choice() picks one element for you. Together these two
  functions can generate a whole random encounter:

      damage = random.randint(5, 15)
      print(f"The {enemy} hits you for {damage}!")

YOUR TASK
  Step 1: Import the random module at the top of your file.
  Step 2: Use random.randint() to roll some damage, and print it.
  Step 3: Create a list of monster names and use random.choice() to
          pick one, then print which monster appeared.
  Step 4: Use a loop to simulate three attacks in a row, printing the
          damage each time.

EXAMPLE
  This example picks a lunch, so you still write your own combat
  rolls.

      import random

      lunches = ["pizza", "pasta", "curry"]
      print(random.choice(lunches))
      for i in range(2):
          print(random.randint(1, 6))

WHEN IT WORKS YOU'LL SEE
  A wild Orc appears!
  Attack 1: 12 damage
  Attack 2: 7 damage
  Attack 3: 15 damage

  (Your numbers will be different every run. That is the point.)

IF YOU GET STUCK
  NameError: random     -> add import random at the top.
  Same number always    -> check you called random.randint() inside
                           the loop, not once before it.
  randint gives too     -> randint(1, 6) includes 6, unlike range.
  high a number

CHECK YOUR WORK
  python run_lesson.py 28
"""

# TODO: Write your code for Lesson 28 below this line.
