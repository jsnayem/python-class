"""
Lesson 24: Error Handling - Surviving Bad Input
================================================

WHAT YOU'LL LEARN
  How to stop your program crashing when the player types something
  silly, and give them a friendly message instead.

NEW WORDS
  exception    An error that happens while the program is running,
               such as trying to turn "banana" into a number.
  ValueError   The specific exception Python raises when a value is
               the wrong sort of thing. int("banana") raises it.
  try          Marks code that might go wrong.
  except       Catches the problem and runs your rescue code instead
               of crashing.
  int()        Turns text into a whole number, when it can.

HOW IT WORKS
  number = int(input("How many? "))

  If the player types 5 this is fine. If they type banana, Python
  raises a ValueError and the whole program stops. Wrap it up:

      def safe_int(prompt):
          try:
              return int(input(prompt))
          except ValueError:
              print("That was not a number. Using 0 instead.")
              return 0

  Python runs the try block. If a ValueError happens anywhere in it,
  it jumps straight to the except block. No crash, and the player
  gets told what went wrong.

  Always name the exception you expect. A bare except: would swallow
  every problem, including the bugs you actually want to hear about.

YOUR TASK
  Step 1: Define a function named safe_int that takes a parameter
          named prompt, asks the player with input(), and uses try
          with except ValueError.
  Step 2: Return the number when it works. When it fails, print an
          error message and return 0.

EXAMPLE
  This example is about an age box, so you still write your own
  safe_int.

      def safe_age(prompt):
          try:
              return int(input(prompt))
          except ValueError:
              print("Ages must be numbers!")
              return 0

WHEN IT WORKS YOU'LL SEE
  How many potions? banana
  That was not a number. Using 0 instead.

IF YOU GET STUCK
  The program still    -> the risky line must be inside the try
  crashes                 block, indented under try:
  SyntaxError          -> both try: and except ValueError: end in a
                          colon and need indented blocks.
  It catches nothing   -> check you wrote except ValueError, matching
                          the error Python actually raises.

STYLE
  Always catch a specific exception like ValueError. Writing a bare
  except: hides real bugs and makes problems much harder to find.

CHECK YOUR WORK
  python run_lesson.py 24
"""

# TODO: Write your code for Lesson 24 below this line.
