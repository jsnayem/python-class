"""
Lesson 4: Math - Calculations
==============================

WHAT YOU'LL LEARN
  How to make Python do sums for you, and store the answers in
  variables so your game can work out damage, healing and treasure.

NEW WORDS
  operator     A symbol that does something to values. + adds,
               - subtracts, * multiplies, / divides.
  expression   A piece of code that works out to a single value, like
               hero_attack - monster_defense.
  evaluate     What Python does to an expression: it works out the
               answer before storing or printing it.

HOW IT WORKS
  hero_attack = 12
  monster_defense = 4
  damage = hero_attack - monster_defense

  Python evaluates the right-hand side first. 12 - 4 is 8, so the
  variable damage now holds 8.

  This is how nearly every game rule is written: take some numbers,
  combine them with operators, and store the result under a clear
  name so you can print it or use it later.

YOUR TASK
  Step 1: Create hero_attack and monster_defense, then work out
          damage = hero_attack - monster_defense and print it.
  Step 2: Create hero_health holding 100, then add 30 to it because
          your hero drank a potion. Print the new health.
          (It should end up as 130.)
  Step 3: Create hero_gold and monster_gold, then add monster_gold
          onto hero_gold because you defeated the monster. Print the
          new total.

EXAMPLE
  This example is about a farm, so you still write your own combat
  maths.

      apples = 10
      eaten = 3
      left = apples - eaten
      print(f"Apples left: {left}")

WHEN IT WORKS YOU'LL SEE
  You hit the monster for 8 damage!
  You drink a potion. Health is now 130
  You loot the monster. Gold is now 85

IF YOU GET STUCK
  TypeError: can only    -> you put quote marks around a number, so
  concatenate str           Python thinks it is text. Numbers do not
                            need quotes.
  The answer never       -> remember to store it back:
  changes                   hero_health = hero_health + 30

CHECK YOUR WORK
  python run_lesson.py 4
"""

# TODO: Write your code for Lesson 4 below this line.
