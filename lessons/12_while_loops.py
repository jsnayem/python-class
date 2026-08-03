"""
Lesson 12: Default Arguments - Optional Information
====================================================

WHAT YOU'LL LEARN
  How to give a parameter a ready-made value, so the person using
  your function can leave it out when they are happy with the usual.

NEW WORDS
  default      A value a parameter falls back to when no argument is
               given. You write it with = in the def line.
  optional     A parameter with a default. The caller may supply it
               or skip it.
  required     A parameter with no default. It must always be given.

HOW IT WORKS
  def greet(name, greeting="Hello"):
      print(f"{greeting}, {name}!")

  name is required; greeting is optional because it already has the
  default "Hello". So both of these work:

      greet("Musab")                    ->  Hello, Musab!
      greet("Musab", "Well met")        ->  Well met, Musab!

  When you leave the second argument out, Python quietly slots in the
  default. Required parameters always come first in the def line;
  Python will complain if you put an optional one before a required
  one.

YOUR TASK
  Step 1: Define a function named greet that takes a required
          parameter named name and an optional parameter named
          greeting whose default value is "Hello".
  Step 2: Call greet once with only a name, and once with both a name
          and a different greeting.

EXAMPLE
  This example is about serving tea, so you still write your own
  greet function.

      def serve(drink, size="medium"):
          print(f"One {size} {drink} coming up!")

      serve("tea")
      serve("coffee", "large")

WHEN IT WORKS YOU'LL SEE
  Hello, Musab!
  Well met, Zoe!

IF YOU GET STUCK
  SyntaxError: non-default  -> a parameter with a default must come
  argument follows default     after all the plain ones.
  The default never shows   -> you passed a second argument every
                               time. Try calling with just the name.

CHECK YOUR WORK
  python run_lesson.py 12
"""

# TODO: Write your code for Lesson 12 below this line.
