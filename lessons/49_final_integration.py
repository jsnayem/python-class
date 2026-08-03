"""
Lesson 49: Final Integration - Putting It All Together
=======================================================

WHAT YOU'LL LEARN
  How to combine the pieces you have built across the whole course
  into the opening of a real game.

NEW WORDS
  integration  Joining separate parts into one working program.
  print_header()  The function you will write to display a framed
               title.
  load_game()  The loader from Lesson 45. You will call it here to
               check for an existing save.
  hero         The variable holding your Hero object. The test looks
               for this exact name.

HOW IT WORKS
  def print_header(text):
      print("=" * 40)
      print(text.center(40))
      print("=" * 40)

  Wrapping the banner from Lesson 47 in a function means you can show
  a header anywhere with one line.

  A real game starts by checking for a save before making anything
  new:

      data = load_game()
      if data is None:
          hero = Hero("Alex")
      else:
          hero = Hero(data["name"])

  Then greet the player by name so they know it worked:

      print_header("GAME START")
      print(f"Welcome, {hero.name}!")

  Everything here is something you already wrote. This lesson is
  about assembling, not inventing.

YOUR TASK
  Step 1: Define a function named print_header that takes text and
          prints it framed by border lines.
  Step 2: Call load_game() to look for an existing save file. Include
          your load_game definition, or a simple version of it, in
          this file.
  Step 3: Create a variable named hero using your Hero class, then
          call print_header and print a welcome that includes the
          hero's name.

EXAMPLE
  This example starts a quiz app, so you still write your own game
  opening.

      def print_title(text):
          print("-" * 20)
          print(text)
          print("-" * 20)

      print_title("QUIZ TIME")
      print(f"Good luck, {player.name}!")

WHEN IT WORKS YOU'LL SEE
  ========================================
                GAME START
  ========================================
  Welcome, Alex! Your adventure begins.

IF YOU GET STUCK
  NameError: Hero       -> paste your Hero class from Lesson 31 into
                           this file too.
  NameError: load_game  -> define load_game here as well, or a short
                           version that returns None.
  The test cannot find  -> name the variable exactly hero.
  your hero

CHECK YOUR WORK
  python run_lesson.py 49
"""

# TODO: Write your code for Lesson 49 below this line.
