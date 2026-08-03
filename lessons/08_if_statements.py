"""
Lesson 8: If Statements - Making Decisions
===========================================

WHAT YOU'LL LEARN
  How to compare numbers and let your game react: warn when health
  is low, celebrate when the hero is rich.

NEW WORDS
  boolean      A value that is either True or False. Nothing else.
  comparison   A question that gives back a boolean. < means "less
               than", > means "greater than", == means "the same as".
  and          Joins two conditions. The whole thing is only True
               when BOTH sides are True.
  or           Joins two conditions. True when EITHER side is True.

HOW IT WORKS
  health = 15
  if health < 20:
      print("Warning! Your health is low.")

  health < 20 is a comparison. Here it works out to True, so the
  indented line runs. If health were 80 it would be False and Python
  would skip straight past.

      if health < 20 and gold > 100:
          print("You are rich but badly hurt. Buy a potion!")

  With and, both halves must be true for the message to appear.

YOUR TASK
  Step 1: Create two variables, health and gold, holding numbers.
  Step 2: Use an if statement to print a warning when health is less
          than 20.
  Step 3: Use another if statement to print a special message when
          gold is greater than 200.
  Step 4: Use one more if statement that combines two conditions with
          and, and print a message when both are true.

EXAMPLE
  This example is about the weather, so you still write your own hero
  checks.

      temperature = 30
      raining = False
      if temperature > 25:
          print("It is hot today.")
      if temperature > 25 and raining == False:
          print("Perfect weather for the beach!")

WHEN IT WORKS YOU'LL SEE
  Warning! Your health is low.
  You are carrying a fortune in gold!

IF YOU GET STUCK
  Nothing prints        -> your numbers may not meet the conditions.
                           Try health = 5 to test the warning.
  SyntaxError           -> every if line ends with a colon :
  IndentationError      -> the message must be indented four spaces
                           under its if.

CHECK YOUR WORK
  python run_lesson.py 8
"""

# TODO: Write your code for Lesson 8 below this line.
