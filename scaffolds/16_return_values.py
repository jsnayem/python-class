"""
Lesson 16: Return Values - Sending An Answer Back
==================================================

WHAT YOU'LL LEARN
  The difference between a function that prints something and a
  function that hands a value back to you, and why handing it back
  is usually better.

NEW WORDS
  return       Sends a value out of the function to whoever called
               it, and stops the function there.
  return value The answer a function gives back.
  None         What a function gives back when it has no return line.
               It means "nothing here".

HOW IT WORKS
  def calculate_heal(amount):
      return amount * 2

  This function does not print. It calculates and returns. The call
  itself becomes worth the answer:

      healed = calculate_heal(15)
      print(healed)

  calculate_heal(15) is worth 30, so healed holds 30. Compare with a
  printing version:

      def show_heal(amount):
          print(amount * 2)

  That one shows the number but hands back None, so you cannot use
  the result in more maths. Returning keeps your options open: you
  can print it, store it, or feed it into another calculation.

YOUR TASK
  Step 1: Define a function named calculate_heal that takes one
          parameter named amount and returns amount * 2.
  Step 2: Call calculate_heal, store the return value in a variable,
          and print it.

EXAMPLE
  This example is about doubling pocket money, so you still write
  your own healing function.

      def double_money(coins):
          return coins * 2

      total = double_money(7)
      print(f"You now have {total} coins.")

WHEN IT WORKS YOU'LL SEE
  Your potion heals 30 health!

IF YOU GET STUCK
  None gets printed    -> your function printed instead of using
                          return, or the return line is missing.
  Nothing prints       -> returning does not show anything. You still
                          need a print() where you call it.
  The code after       -> return stops the function immediately. Put
  return never runs       it last.

STYLE
  Prefer return over print inside a function. A function that returns
  a value can be reused anywhere; one that only prints is stuck doing
  just that one thing.

CHECK YOUR WORK
  python run_lesson.py 16
"""

# TODO: Write your code for Lesson 16 below this line.
