"""
Lesson 1: Hello, World! - Your First Program
=============================================

WHAT YOU'LL LEARN
  How to make the computer show words on the screen.

NEW WORDS
  program    A list of instructions for the computer, written in order
             from top to bottom.
  print()    A built-in instruction that shows something on the screen.
             The round brackets () hold the thing you want to show.
  string     Text in a program. You wrap text in quote marks so Python
             knows it is words and not code, like "Hello".
  run        To make the computer actually do your instructions.

HOW IT WORKS
  print("Hello, Adventurer!")

  Read it as: "print the words Hello, Adventurer! on the screen."
  The quote marks are not shown to the player. They only tell Python
  where the text starts and where it ends.

  Python runs your lines one at a time, from the top down. Three
  print() lines make three lines appear on the screen.

YOUR TASK
  Step 1: Use print() to show a greeting that says hello to the
          adventurer.
  Step 2: Use print() on the next line to show your name.
  Step 3: Use print() on the next line to show a fun fact about you.

EXAMPLE
  This example is about a robot, so you still write your own three
  lines about you.

      print("Beep boop, I am a robot.")
      print("My name is Rusty")
      print("I am made of tin")

WHEN IT WORKS YOU'LL SEE
  Hello, Adventurer!
  My name is Musab
  I love dragons!

IF YOU GET STUCK
  SyntaxError                -> you probably missed a quote mark or a
                                round bracket. Every " needs a partner.
  NameError: name is not     -> you forgot the quote marks, so Python
  defined                       thought your words were code.
  Nothing appears            -> did you spell print correctly, all in
                                small letters?

CHECK YOUR WORK
  python run_lesson.py 1
"""

# TODO: Write your code for Lesson 1 below this line.
print("Hello, Adventurer!")
print("My name is Alex")
print("I love dragons!")