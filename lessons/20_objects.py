"""
Lesson 20: Objects Interacting - A Simple Attack
=================================================

WHAT YOU'LL LEARN
  How to change an object's information from outside it, so two
  things in your game can affect each other.

NEW WORDS
  method       A function that belongs to a class. It always takes
               self first, and is called with a dot.
  state        The current values stored on an object, such as how
               much health a goblin has left right now.
  mutate       To change an object's state, for example lowering its
               health when it is hit.

HOW IT WORKS
  class Goblin:
      def __init__(self):
          self.health = 30

  Every Goblin starts with 30 health. A function can reach into the
  object and change that:

      def attack(goblin):
          goblin.health = goblin.health - 10
          print(f"You hit the goblin! It has {goblin.health} health left.")

  Because goblin.health lives on the object, the change sticks. Call
  attack twice and the health drops twice. This is the heart of every
  battle system: one thing changes another thing's state.

YOUR TASK
  Step 1: Create a class named Goblin whose __init__ gives it a
          health attribute.
  Step 2: Write a function named attack that takes a goblin, lowers
          its health, and prints how much is left.
  Step 3: Create a Goblin, call attack on it, and print the result.

EXAMPLE
  This example is about a piggy bank, so you still write your own
  goblin battle.

      class PiggyBank:
          def __init__(self):
              self.coins = 20

      def spend(bank):
          bank.coins = bank.coins - 5
          print(f"Coins left: {bank.coins}")

      piggy = PiggyBank()
      spend(piggy)

WHEN IT WORKS YOU'LL SEE
  You hit the goblin! It has 20 health left.

IF YOU GET STUCK
  AttributeError        -> __init__ must set self.health, otherwise
                           the goblin has no health to lower.
  Health never changes  -> store the result back:
                           goblin.health = goblin.health - 10
  TypeError             -> attack needs the goblin passed in:
                           attack(goblin)

CHECK YOUR WORK
  python run_lesson.py 20
"""

# TODO: Write your code for Lesson 20 below this line.
