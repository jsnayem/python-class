"""
Lesson 29: Time - Slowing Things Down
======================================

WHAT YOU'LL LEARN
  How to pause your program on purpose, so messages appear
  dramatically instead of all at once.

NEW WORDS
  time          A module for working with time.
  time.sleep(1) Pauses the program for one second. You can use
                decimals, like 0.5 for half a second.
  suspense      The effect you get by pausing between messages, which
                makes a game feel alive.

HOW IT WORKS
  import time

  print("The dragon stirs...")
  time.sleep(1)
  print("It opens one enormous eye.")

  Python prints the first line, waits a full second doing nothing,
  then prints the second. To the player it feels like the game is
  thinking.

  Short pauses work best. Half a second between combat messages keeps
  it readable; five seconds is annoying.

      for i in range(3):
          print(f"Charging... {i + 1}")
          time.sleep(0.5)

YOUR TASK
  Step 1: Import the time module at the top of your file.
  Step 2: Print a few dramatic messages with time.sleep() between
          them, so they appear one after another instead of all at
          once.

EXAMPLE
  This example is a countdown, so you still write your own dramatic
  scene.

      import time

      for i in range(3, 0, -1):
          print(i)
          time.sleep(0.5)
      print("Go!")

WHEN IT WORKS YOU'LL SEE
  The dragon stirs...
  (one second passes)
  It opens one enormous eye.
  (one second passes)
  Run!

IF YOU GET STUCK
  NameError: time       -> add import time at the top of the file.
  Nothing pauses        -> you wrote time.sleep(1) without brackets,
                           or used sleep(1) without the time. part.
  Everything appears    -> the pauses are working, they are just very
  instantly                short. Try 1 instead of 0.05.

CHECK YOUR WORK
  python run_lesson.py 29
"""

# TODO: Write your code for Lesson 29 below this line.
