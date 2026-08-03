"""
Lesson 50: Play And Share - You Did It
=======================================

WHAT YOU'LL LEARN
  How to finish your project properly: a completion message and a
  credits screen, just like a real game.

NEW WORDS
  credits      The exact name of the function you will write. Real
               games list who made them at the end.
  call         Defining credits() is not enough. You must also run it
               with credits() on its own line.
  ship         What programmers say when a project is finished and
               handed to real people.

HOW IT WORKS
  def credits():
      print("DRAGON QUEST")
      print("Programmed by: Musab")
      print("Thanks for playing!")

  A function groups the credits so you can show them whenever the
  game ends. Remember that defining it does nothing on its own:

      credits()

  That separate line is what actually runs it. Print a completion
  message too, so the whole file produces at least three lines of
  output when it runs.

YOUR TASK
  Step 1: Print a completion message saying you finished the course.
  Step 2: Define a function named credits that prints your game's
          title and your name, then call credits() to run it.
  Step 3: Make sure your program prints at least three lines in
          total, saying something you are proud of.

EXAMPLE
  This example ends a puzzle app, so you still write your own
  credits.

      print("Puzzle complete!")

      def credits():
          print("PUZZLE MASTER")
          print("Made by: Sam")

      credits()

WHEN IT WORKS YOU'LL SEE
  You have completed all 50 lessons!
  DRAGON QUEST
  Programmed by: Musab
  Thanks for playing!

IF YOU GET STUCK
  Nothing prints from   -> you defined credits but never called it.
  credits                  Add credits() on its own line.
  Not enough lines      -> print a completion message as well as the
                           credits.
  IndentationError      -> the call to credits() must not be indented
                           under the def.

CHECK YOUR WORK
  python run_lesson.py 50

  Then play your game:  python main.py
  You built this. Well done.
"""

# TODO: Write your code for Lesson 50 below this line.
