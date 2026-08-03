"""
Lesson 14: Calling A Function Many Times
=========================================

WHAT YOU'LL LEARN
  Why writing a function once and calling it repeatedly is far better
  than copying and pasting the same lines over and over.

NEW WORDS
  call         To make a function run, by writing its name followed
               by round brackets.
  reuse        Using the same function again instead of writing new
               copies of the same code.
  DRY          A rule real programmers follow: Don't Repeat Yourself.
               If you are copying code, write a function instead.

HOW IT WORKS
  def cast_spell(spell_name):
      print(f"You cast {spell_name}! Sparks fly everywhere.")

  Now one line of code produces a whole message, and you can produce
  as many as you like:

      cast_spell("Fireball")
      cast_spell("Ice Blast")
      cast_spell("Healing Light")

  Three calls, three different messages, but only one copy of the
  printing code. If you later want to change the wording, you change
  it in one place and every call improves at once. That is why DRY
  matters.

YOUR TASK
  Step 1: Define a function named cast_spell that takes one parameter
          named spell_name and prints a message using it.
  Step 2: Call cast_spell three times, each with a different spell.

EXAMPLE
  This example is about feeding pets, so you still write your own
  spell function.

      def feed_pet(pet):
          print(f"You feed {pet}. It looks happy!")

      feed_pet("the cat")
      feed_pet("the dog")
      feed_pet("the dragon")

WHEN IT WORKS YOU'LL SEE
  You cast Fireball! Sparks fly everywhere.
  You cast Ice Blast! Sparks fly everywhere.
  You cast Healing Light! Sparks fly everywhere.

IF YOU GET STUCK
  Only one message      -> you need three separate call lines, not
                           one call inside the function.
  The same spell every  -> pass a different argument in each call.
  time

CHECK YOUR WORK
  python run_lesson.py 14
"""

# TODO: Write your code for Lesson 14 below this line.
