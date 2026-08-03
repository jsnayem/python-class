"""
Lesson 13: For Loops - Doing Something To Every Item
=====================================================

WHAT YOU'LL LEARN
  How to use a for loop to run the same code once for every item in
  a list, and how to repeat something a fixed number of times.

NEW WORDS
  for          Starts a loop that visits each item in a collection.
  iterate      The proper word for going through a collection one
               item at a time. A for loop iterates over a list.
  range(3)     A built-in that counts for you: 0, then 1, then 2.
               It stops before the number you give it.
  loop variable  The name between for and in. Each time round, Python
               puts the next item into it.

HOW IT WORKS
  for item in inventory:
      print(item)

  Read it as: "for each item in inventory, print that item." Python
  repeats the indented block once per element, putting the next
  element into item every time. You never say how many items there
  are; the loop works that out.

      for i in range(3):
          print(i)

  This prints 0, 1 and 2. range(3) means three numbers starting at
  zero, which is how programmers usually count.

  The colon at the end of the for line and the four-space indent
  underneath are both required. They tell Python which lines repeat.

YOUR TASK
  Step 1: Create a list named inventory holding three items you like.
  Step 2: Use a for loop to print each item in inventory on its own
          line.
  Step 3: Use for i in range(3) to print three numbers.

EXAMPLE
  This example is about spells, so you still write your own inventory
  loop.

      spells = ["Fireball", "Heal", "Shield"]
      for spell in spells:
          print(f"Casting {spell}!")

      for i in range(2):
          print(i)

WHEN IT WORKS YOU'LL SEE
  Iron Sword
  Health Potion
  Wooden Shield
  0
  1
  2

IF YOU GET STUCK
  IndentationError    -> the line after the colon must be indented
                         four spaces.
  Nothing prints      -> your list may be empty, or the print() is
                         outside the loop.
  TypeError: not      -> you wrote for i in 3. You need range(3).
  iterable

CHECK YOUR WORK
  python run_lesson.py 13
"""

# TODO: Write your code for Lesson 13 below this line.
