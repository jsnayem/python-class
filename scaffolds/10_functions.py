"""
Lesson 10: Functions - Naming A Job
====================================

WHAT YOU'LL LEARN
  How to wrap up some code, give it a name, and use it as many times
  as you like without copying and pasting.

NEW WORDS
  function     A named piece of code that does one job. You create it
               with def and use it by writing its name with brackets.
  def          The keyword that defines a function.
  parameter    A name in the function's brackets that stands for
               information the function needs.
  argument     The actual value you hand over when you call it.
  call         To make a function run: show_status("Musab", 100, 50)
  return       Sends a value back to whoever called the function.
  docstring    A short string just under def that says what the
               function does.

HOW IT WORKS
  def show_status(name, health, gold):
      \"\"\"Print one line describing a hero.\"\"\"
      print(f"{name}: {health} HP, {gold} gold")

  Nothing happens when you define a function. It only runs when you
  call it:

      show_status("Musab", 100, 50)

  Here name, health and gold are parameters; "Musab", 100 and 50 are
  the arguments. Some functions hand an answer back instead of
  printing:

      def calculate_damage(base, bonus):
          \"\"\"Return the total damage of an attack.\"\"\"
          return base + bonus

  Now calculate_damage(10, 5) is worth 15 wherever you write it.

YOUR TASK
  Step 1: Define a function named show_status that takes three
          parameters: name, health and gold, and prints them.
  Step 2: Call show_status twice, for two different heroes.
  Step 3: Define a function named calculate_damage that takes base
          and bonus, and returns base + bonus. Call it and print the
          result.

EXAMPLE
  This example is about greeting a customer, so you still write your
  own hero functions.

      def greet_customer(name):
          \"\"\"Welcome one customer by name.\"\"\"
          print(f"Welcome, {name}!")

      greet_customer("Ada")
      greet_customer("Grace")

WHEN IT WORKS YOU'LL SEE
  Musab: 100 HP, 50 gold
  Zoe: 80 HP, 120 gold
  Total damage: 15

IF YOU GET STUCK
  Nothing happens       -> defining is not calling. Add a line that
                           calls the function by name.
  TypeError: missing    -> you called it with fewer arguments than it
  argument                 has parameters.
  None gets printed     -> your function printed instead of using
                           return, or you forgot the return line.

STYLE
  Give every function a docstring, and make each function do one job.
  A function named calculate_damage should work out damage and hand
  it back, not print it. That way you can reuse it anywhere.

CHECK YOUR WORK
  python run_lesson.py 10
"""

# TODO: Write your code for Lesson 10 below this line.
