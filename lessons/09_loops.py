"""
Lesson 9: Loops - Repeating Without Retyping
=============================================

WHAT YOU'LL LEARN
  Two ways to repeat code: a while loop that keeps going until
  something changes, and a for loop that visits every item in a list.

NEW WORDS
  loop         Code that runs more than once.
  while        Repeats for as long as a condition stays True.
  for          Repeats once for each item in a collection.
  iterate      The proper word for going through a collection one
               item at a time.
  += 1         A shortcut for "add one to this variable".
               count += 1 means count = count + 1.

HOW IT WORKS
  count = 1
  while count <= 5:
      print(count)
      count += 1

  Python checks the condition, runs the indented block, then checks
  again. The count += 1 line is vital: without it the condition never
  becomes False and the loop runs forever.

      for item in inventory:
          print(item)

  A for loop needs no counter. It hands you each element in turn.

YOUR TASK
  Step 1: Use a while loop to print the numbers 1 to 5.
  Step 2: Create a list named inventory with a few items, then use a
          for loop to print each one.
  Step 3: Use a while loop that runs while health is above 0,
          subtracting some damage each time, to simulate a fight.

EXAMPLE
  This example is a countdown for a rocket, so you still write your
  own counting and combat.

      seconds = 3
      while seconds > 0:
          print(seconds)
          seconds -= 1
      print("Lift off!")

WHEN IT WORKS YOU'LL SEE
  1
  2
  3
  4
  5
  Health Potion
  Iron Sword
  The monster hits you! Health is now 80

IF YOU GET STUCK
  The program freezes   -> your while loop never ends. Make sure the
                           variable in the condition changes inside
                           the loop.
  IndentationError      -> everything that repeats must be indented
                           under the loop line.

CHECK YOUR WORK
  python run_lesson.py 9
"""

# TODO: Write your code for Lesson 9 below this line.
