"""
Lesson 11: Functions - Making a Spell
======================================

WHAT YOU'LL LEARN
  How to write your own function that takes information in, so one
  piece of code can behave differently every time you use it.

NEW WORDS
  define       To create a function using the def keyword. Defining
               does not run it; it only teaches Python the recipe.
  parameter    The name inside the brackets of a def line. It is a
               empty slot waiting to be filled when the function runs.
  argument     The real value you put in that slot when you call it.
  body         The indented lines underneath def. This is the code
               that runs each time you call the function.

HOW IT WORKS
  def cast_fireball(damage):
      print(f"A fireball roars out and deals {damage} damage!")

  The word damage in the brackets is a parameter. Inside the body it
  behaves like a normal variable. When you call the function:

      cast_fireball(30)

  Python copies 30 into damage and runs the body, so it prints
  "deals 30 damage". Call it again with a different argument and you
  get a different message from the very same code:

      cast_fireball(75)

  That is the whole point of a parameter. Write the spell once, use
  it at any power.

YOUR TASK
  Step 1: Define a function named cast_fireball that takes one
          parameter named damage, and prints a fireball message that
          includes the damage number.
  Step 2: Call cast_fireball at least twice, each time with a
          different damage amount.

EXAMPLE
  This example is about a drum, so you still write your own spell.

      def bang_drum(times):
          print(f"You bang the drum {times} times!")

      bang_drum(3)
      bang_drum(10)

WHEN IT WORKS YOU'LL SEE
  A fireball roars out and deals 30 damage!
  A fireball roars out and deals 75 damage!

IF YOU GET STUCK
  Nothing happens        -> you defined the function but never called
                            it. A call is a separate line with no def.
  TypeError: missing 1   -> you called cast_fireball() with empty
  required argument         brackets. It needs a damage number.
  NameError              -> check the spelling of the function name
                            matches in both the def and the call.

CHECK YOUR WORK
  python run_lesson.py 11
"""

# TODO: Write your code for Lesson 11 below this line.
