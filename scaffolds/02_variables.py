"""
Lesson 2: Variables - Storing Information
==========================================

WHAT YOU'LL LEARN
  How to give a name to a piece of information so you can use it
  again later, and change it.

NEW WORDS
  variable   A name that holds a value, like a labelled box. You put
             something in the box now and open it later.
  =          The assignment operator. It does NOT mean "equals" like
             in maths. It means "put the value on the right into the
             name on the left."
  integer    A whole number with no decimal point, like 100 or 50.
             Programmers say "int" for short.
  f-string   A string with an f in front of it. Inside it you can put
             a variable in curly brackets {} and Python swaps in the
             value for you.

HOW IT WORKS
  hero_health = 100

  This creates a box named hero_health with 100 inside it. From now
  on, writing hero_health means 100.

      print(f"Health: {hero_health}")

  The f before the quote lets you drop a variable straight into the
  text. Python replaces {hero_health} with 100 before printing.

  You can also change what is in the box:

      hero_health = hero_health + 25

  Python works out the right-hand side first (100 + 25), then puts
  the answer back into the box. The box now holds 125.

YOUR TASK
  Step 1: Create three variables:
            hero_name   holding your hero's name as a string
            hero_health holding the number 100
            hero_gold   holding the number 50
  Step 2: Print all three values using f-strings.
  Step 3: Add 20 to hero_gold, then print the new total.
          (After this your hero should have 70 gold.)

EXAMPLE
  This example is about a spaceship, so you still write your own
  hero code.

      ship_name = "Falcon"
      ship_fuel = 40
      print(f"The {ship_name} has {ship_fuel} fuel.")
      ship_fuel = ship_fuel + 10
      print(f"After refuelling: {ship_fuel} fuel.")

WHEN IT WORKS YOU'LL SEE
  Hero: Musab
  Health: 100
  Gold: 50
  After finding treasure, gold is now 70

IF YOU GET STUCK
  NameError            -> you used a variable before creating it, or
                          spelled the name differently. Names must
                          match exactly, including capital letters.
  Curly brackets show  -> you forgot the f before the opening quote.
  up in the output

STYLE
  Real programmers write variable names in snake_case: all small
  letters with underscores between words, like hero_health. The name
  should say what is inside. hero_health is good; hh is not.

CHECK YOUR WORK
  python run_lesson.py 2
"""

# TODO: Write your code for Lesson 2 below this line.
