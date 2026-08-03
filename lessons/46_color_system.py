r"""
Lesson 46: Colors - Making The Terminal Glow
=============================================

WHAT YOU'LL LEARN
  How terminals show colored text, and how to wrap your own messages
  in color safely.

NEW WORDS
  ANSI escape code  A short secret string that tells the terminal to
               change color. They all begin with \033[ which is the
               escape character followed by a square bracket.
  Color        The class you will write to hold those codes.
  constant     A value that never changes. Constants are written in
               UPPER_CASE, like RED and RESET.
  RESET        The code that turns the color back to normal. Without
               it, everything printed afterwards stays colored.
  colorize()   The function you will write to wrap text in a color.

HOW IT WORKS
  class Color:
      RED = "\033[91m"
      GREEN = "\033[92m"
      YELLOW = "\033[93m"
      RESET = "\033[0m"

  These live in the class body as class attributes, so you reach them
  as Color.RED from anywhere. Then one small function does the work:

      def colorize(text, color):
          return color + text + Color.RESET

  Always finish with Color.RESET. If you forget, the color leaks and
  every later line in the player's terminal comes out red.

      print(colorize("Danger!", Color.RED))

YOUR TASK
  Step 1: Create a class named Color holding escape-code constants,
          including at least one color and a RESET code.
  Step 2: Define a function named colorize that takes text and color,
          and returns the text wrapped in that color and ending with
          Color.RESET.
  Step 3: Print a colored message using colorize.

EXAMPLE
  This example is a traffic light, so you still write your own Color
  class.

      class Light:
          STOP = "\033[91m"
          OFF = "\033[0m"

      def paint(word, code):
          return code + word + Light.OFF

      print(paint("STOP", Light.STOP))

WHEN IT WORKS YOU'LL SEE
  A red "Danger!" and a green "You found treasure!" in your terminal.
  If the colors look like odd symbols instead, your terminal does not
  support them, but the test will still pass.

IF YOU GET STUCK
  Everything stays      -> you forgot Color.RESET at the end of
  colored afterwards       colorize.
  AttributeError:       -> the constants must be inside the class
  RESET                    body, not inside a method.
  The codes print as    -> use \033[ exactly, with a backslash, zero,
  plain text               three, three.

STYLE
  Values that never change are written in UPPER_CASE. Seeing
  Color.RED tells a reader instantly that it is a fixed constant, not
  a variable that might be reassigned.

CHECK YOUR WORK
  python run_lesson.py 46
"""

# TODO: Write your code for Lesson 46 below this line.
