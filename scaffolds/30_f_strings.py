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
  hero = "Musab"
  hp = 87.5
  gold = 120

  print(f"{hero} has {hp} health")

  You can put a whole calculation inside the brackets too:

      print(f"Half health is {hp / 2}")

  For neat columns, add a format spec after a colon:

      print(f"{hero:<10}{hp:.1f}")

  The :<10 pads the name out to ten characters so several rows line
  up underneath each other, and :.1f trims a long decimal down to one
  place. This is how you make a status table that does not look
  ragged.

YOUR TASK
  Step 1: Create three variables named exactly hero (a string), hp
          and gold (numbers).
  Step 2: Print a status table of at least two rows using f-strings,
          showing the hero, hp and gold values.
  Step 3: Use a format spec such as :<10 or :.1f to line up or tidy
          the values into columns.

EXAMPLE
  This example is a race result, so you still write your own hero
  table.

      runner = "Zoe"
      seconds = 12.4567
      print(f"{runner:<8}{seconds:.2f} seconds")
      print(f"{'Total':<8}{seconds * 2:.2f} seconds")

WHEN IT WORKS YOU'LL SEE
  Hero      Musab
  HP        87.5
  Gold      120

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
