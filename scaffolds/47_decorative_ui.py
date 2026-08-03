"""
Lesson 47: Decorative UI - A Banner Worth Looking At
=====================================================

WHAT YOU'LL LEARN
  How to frame your game's title so it looks like a real product
  instead of plain text.

NEW WORDS
  banner       A title framed by decorative lines.
  border       A line made by repeating one character, like
               "=" * 40. It must contain no letters or numbers.
  separator    Another line below the title, dividing it from what
               comes next.
  .center()    A string method that pads text with spaces so it sits
               in the middle of a given width.

HOW IT WORKS
  print("=" * 40)
  print("DRAGON QUEST".center(40))
  print("=" * 40)

  Three lines: a border, a title, and a separator. The border is
  forty = characters. Because "=" * 40 repeats a single character, it
  counts as a proper border line.

  .center(40) pads the title with spaces on both sides so it sits in
  the middle of the same forty-character width, which is what makes
  the banner look deliberate rather than lopsided.

  Try other characters for a different mood: * or - or ~ all work.

YOUR TASK
  Step 1: Print a border line made by repeating one character at
          least five times, then print a title with words in it.
  Step 2: Print another separator line underneath, so your banner has
          at least three lines in total.

EXAMPLE
  This example is a cinema sign, so you still write your own game
  banner.

      print("*" * 30)
      print("NOW SHOWING".center(30))
      print("*" * 30)

WHEN IT WORKS YOU'LL SEE
  ========================================
               DRAGON QUEST
  ========================================

IF YOU GET STUCK
  Your border does not  -> a border must be one repeated character
  count                    with no letters or numbers in it.
  Not enough lines      -> you need at least three printed lines:
                           border, title, separator.
  The title is not      -> .center() needs the same width as your
  centred                  border, for example .center(40).

CHECK YOUR WORK
  python run_lesson.py 47
"""

# TODO: Write your code for Lesson 47 below this line.
