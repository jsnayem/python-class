"""
Lesson 5: Strings - Working With Text
======================================

WHAT YOU'LL LEARN
  How to join pieces of text together and how to change text into
  capitals or small letters.

NEW WORDS
  method        An instruction that belongs to a value and is written
                after a dot, like monster_name.upper().
  .upper()      A string method that gives back a SHOUTY copy of the
                text, in capitals.
  .lower()      A string method that gives back a quiet copy, all in
                small letters.
  concatenate   The proper word for joining strings together to make
                one longer string.

HOW IT WORKS
  monster_name = "goblin"
  print(monster_name.upper())

  This prints GOBLIN. Note that .upper() does not change the box: the
  variable still holds "goblin". Methods give you back a new value.

      print(f"A {monster_name} appears! {monster_desc}")

  An f-string is the neatest way to concatenate: you write the
  sentence once and drop the variables in where you need them.

YOUR TASK
  Step 1: Create two variables, monster_name and monster_desc, both
          holding strings.
  Step 2: Print one message that contains both the name and the
          description together.
  Step 3: Print monster_name.upper() and print monster_name.lower().

EXAMPLE
  This example is about a pet, so you still write your own monster.

      pet_name = "Rex"
      pet_desc = "a very loud dog"
      print(f"Meet {pet_name}, {pet_desc}.")
      print(pet_name.upper())
      print(pet_name.lower())

WHEN IT WORKS YOU'LL SEE
  A goblin appears! It is small, green and grumpy.
  GOBLIN
  goblin

IF YOU GET STUCK
  AttributeError       -> .upper() only works on strings. Check you
                          are not calling it on a number.
  Nothing changed      -> .upper() gives back a new string; you have
                          to print it or store it.

CHECK YOUR WORK
  python run_lesson.py 5
"""

# TODO: Write your code for Lesson 5 below this line.
