"""
Lesson 30: F-Strings - Neat, Readable Output
=============================================

WHAT YOU'LL LEARN
  How to build tidy lines of text with values slotted in, and how to
  line things up so your status screens look professional.

NEW WORDS
  f-string     A string with f before the opening quote. Anything in
               curly brackets is worked out and slotted in.
  placeholder  The {} part inside an f-string.
  format spec  Extra instructions after a colon inside the brackets,
               controlling width or decimal places.
  :<10         Pad this value with spaces to ten characters wide,
               lined up to the left.
  :.1f         Show this number with one digit after the point.

HOW IT WORKS
  name = "Musab"
  health = 87.5

  print(f"{name} has {health} health")

  You can put a whole calculation inside the brackets too:

      print(f"Half health is {health / 2}")

  For neat columns, add a format spec after a colon:

      print(f"{name:<10}{health:.1f}")

  The :<10 pads the name out to ten characters so several rows line
  up underneath each other, and :.1f trims a long decimal down to one
  place. This is how you make a status table that does not look
  ragged.

YOUR TASK
  Step 1: Create variables for a hero's name and some numbers.
  Step 2: Print a status line using an f-string with at least two
          placeholders in it.
  Step 3: Use a format spec such as :<10 or :.1f to line up or tidy
          one of the values.

EXAMPLE
  This example is a race result, so you still write your own hero
  status.

      runner = "Zoe"
      seconds = 12.4567
      print(f"{runner:<8}{seconds:.2f} seconds")

WHEN IT WORKS YOU'LL SEE
  Musab     87.5
  Zoe       64.0

IF YOU GET STUCK
  The brackets print    -> you forgot the f before the opening quote.
  literally
  ValueError: invalid   -> check the format spec. Use :.1f for
  format spec              decimals and :<10 for width.
  TypeError             -> :.1f only works on numbers, not strings.

CHECK YOUR WORK
  python run_lesson.py 30
"""

# TODO: Write your code for Lesson 30 below this line.
