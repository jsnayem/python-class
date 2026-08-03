"""
Lesson 6: Input - Talking To The Player
========================================

WHAT YOU'LL LEARN
  How to ask the player a question and use their answer, and how to
  make your program do different things depending on that answer.

NEW WORDS
  input()      A built-in instruction that stops and waits for the
               player to type something and press Enter. Whatever
               they typed comes back as a string.
  prompt       The message you show inside input() so the player
               knows what to type.
  if           A keyword that runs some code only when something is
               true.
  ==           The comparison operator meaning "is the same as".
               One = stores a value; two == asks a question.
  condition    The true-or-false question an if statement asks.

HOW IT WORKS
  hero_name = input("What is your name? ")

  The program pauses, the player types, and their answer lands in
  the variable hero_name.

      choice = input("Attack or flee? ")
      if choice == "a":
          print("You swing your sword!")

  The if line asks a question. The indented line below it only runs
  when the answer is yes. Notice the colon at the end of the if line
  and the four-space indent underneath: both are required.

YOUR TASK
  Step 1: Use input() to ask the player for their hero's name and
          store it in a variable.
  Step 2: Use input() a second time to ask what they want to do.
          Tell them to type "a" to attack or "f" to flee.
  Step 3: Use an if statement to check the answer, and print a
          different message for attacking and for fleeing.

EXAMPLE
  This example is about ordering a drink, so you still write your own
  battle choice.

      name = input("Your name? ")
      drink = input("Tea or coffee? Type t or c: ")
      if drink == "t":
          print(f"One tea for {name}!")
      if drink == "c":
          print(f"One coffee for {name}!")

WHEN IT WORKS YOU'LL SEE
  What is your name? Musab
  Type a to attack or f to flee: a
  Musab swings a mighty sword!

IF YOU GET STUCK
  IndentationError      -> the line under if must be indented by four
                           spaces.
  Nothing happens when  -> you used one = instead of two == in the
  you type a               if line.
  It never matches      -> input() always gives a string. Compare
                           against "a" with quotes, not a with none.

CHECK YOUR WORK
  python run_lesson.py 6
"""

# TODO: Write your code for Lesson 6 below this line.
