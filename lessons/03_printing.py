r"""
Lesson 3: Printing with Style
==============================

WHAT YOU'LL LEARN
  How to lay text out neatly using special codes for new lines and
  for tabs, so your game looks tidy instead of squashed.

NEW WORDS
  escape sequence  Two characters starting with a backslash that mean
                   something special inside a string.
  \n               Newline. Where you put it, the text jumps down to
                   the next line.
  \t               Tab. Adds a wide gap, useful for lining up columns.
  border           A decorative line, usually made by repeating one
                   character, that separates parts of the screen.

HOW IT WORKS
  print("=" * 30)

  The * repeats a string. "=" * 30 makes a line of thirty = signs,
  which is a quick way to draw a border.

      print("Name:\tMusab")

  The \t puts a tab gap between Name: and Musab, so several lines
  line up in a column.

      print("Top line\n\nBottom line")

  Two \n in a row leave a completely blank line between the two
  pieces of text.

YOUR TASK
  Step 1: Print a title with a border made of = characters above or
          below it.
  Step 2: Use \n somewhere to create a blank line, and use \t
          somewhere to make a gap.
  Step 3: Print your hero's health and gold together on one line, so
          that line contains both numbers.

EXAMPLE
  This example is about a pizza shop, so you still write your own
  hero display.

      print("=" * 20)
      print("PIZZA MENU")
      print("=" * 20)
      print("Cheese:\t5 coins\n")
      print("Total today: 12 sold, 3 left")

WHEN IT WORKS YOU'LL SEE
  ==============================
  HERO STATUS
  ==============================
  Health:	100	Gold:	70

  Ready for adventure!

IF YOU GET STUCK
  \n shows as letters  -> you typed it outside the quote marks, or
                         used a forward slash / instead of a
                         backslash \.
  Everything on one    -> you have no \n and no separate print()
  line                    calls.

CHECK YOUR WORK
  python run_lesson.py 3
"""

# TODO: Write your code for Lesson 3 below this line.
