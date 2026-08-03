"""
Lesson 37: The Monster Class - Something To Fight
==================================================

WHAT YOU'LL LEARN
  How to build the Monster class, including a method that takes a hit
  and never lets health fall below zero.

NEW WORDS
  attack_power  How hard this monster hits.
  gold_reward   How much gold the hero wins for defeating it.
  take_damage() A method that lowers the monster's health.
  max()         A built-in that gives the larger of two numbers.
                max(x, 0) is the neat way to stop a value going
                negative.

HOW IT WORKS
  class Monster:
      def __init__(self, name, health, attack_power, gold_reward):
          self.name = name
          self.health = health
          self.attack_power = attack_power
          self.gold_reward = gold_reward

  Every monster is different, so all four are parameters. Note the
  order carefully: name, health, attack_power, gold_reward.

      def take_damage(self, damage):
          self.health = max(self.health - damage, 0)

      def is_alive(self):
          return self.health > 0

  max(self.health - damage, 0) means "whichever is bigger: the new
  health, or zero." A monster on 5 health hit for 100 lands on 0, not
  -95, which would look silly on screen.

YOUR TASK
  Step 1: Create a class named Monster whose __init__ takes self,
          name, health, attack_power and gold_reward, in that order,
          and stores all four.
  Step 2: Add a method named take_damage that lowers health but never
          below 0, and a method named is_alive that returns True
          while health is above 0.
  Step 3: Create a Goblin with 30 health, print its HP, hit it, and
          print its HP again.

EXAMPLE
  This example is a pinata, so you still write your own Monster.

      class Pinata:
          def __init__(self, sweets):
              self.sweets = sweets

          def whack(self, amount):
              self.sweets = max(self.sweets - amount, 0)

      p = Pinata(10)
      p.whack(4)
      print(p.sweets)

WHEN IT WORKS YOU'LL SEE
  A Goblin appears with 30 HP!
  You strike it for 10. The Goblin has 20 HP left.

IF YOU GET STUCK
  Health goes negative  -> wrap it in max(..., 0).
  TypeError: missing    -> Monster needs all four arguments in the
  arguments                right order.
  is_alive gives None   -> you forgot return.

CHECK YOUR WORK
  python run_lesson.py 37
"""

# TODO: Write your code for Lesson 37 below this line.
