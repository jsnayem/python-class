"""
Lesson 40: The Flee Mechanic - Running Away
============================================

WHAT YOU'LL LEARN
  How to give the player a risky escape option using a chance, and
  how a default argument makes that chance adjustable.

NEW WORDS
  flee         The exact name of the function you will write.
  chance       A probability between 0.0 and 1.0. 0.5 means a
               fifty-fifty coin flip.
  random.random()  Gives a decimal from 0.0 up to just below 1.0.
  probability  How likely something is. Comparing a random number
               against your chance is how you roll for it.

HOW IT WORKS
  import random

  def flee(chance=0.5):
      return random.random() < chance

  random.random() produces something like 0.31 or 0.87. Asking
  whether it is below chance is already True or False, so you can
  return the comparison directly.

  Think about why this works. With chance 0.5, half of all possible
  random values fall below 0.5, so you escape half the time. Set
  chance to 1.0 and every value is below it, so you always escape.
  Set it to 0.0 and nothing is below it, so you never do.

  Because chance has a default, flee() works with no arguments at
  all, but flee(chance=0.9) makes a desperate hero luckier.

YOUR TASK
  Step 1: Import random, then define a function named flee with one
          optional parameter named chance whose default is 0.5.
  Step 2: Return True or False by comparing random.random() against
          chance, so that a chance of 1.0 always escapes and 0.0
          never does.
  Step 3: Call flee a few times in a loop and print whether the hero
          got away each time.

EXAMPLE
  This example is a raffle, so you still write your own flee.

      import random

      def wins_prize(odds=0.1):
          return random.random() < odds

      for i in range(3):
          print(wins_prize(0.5))

WHEN IT WORKS YOU'LL SEE
  You try to flee... escaped!
  You try to flee... the Goblin blocks your path!
  You try to flee... escaped!

  (Your results change every run, because it is random.)

IF YOU GET STUCK
  It always returns     -> use < (less than), not > . With >, a
  the wrong thing          chance of 1.0 would never escape.
  TypeError: flee()     -> chance needs a default: def flee(chance=0.5)
  missing argument
  NameError: random     -> add import random at the top.

CHECK YOUR WORK
  python run_lesson.py 40
"""

# TODO: Write your code for Lesson 40 below this line.
