"""
Lesson 39: The Damage Formula - Attack Minus Defense
=====================================================

WHAT YOU'LL LEARN
  How to write the calculation that decides how much a hit hurts,
  and how to stop it ever being useless.

NEW WORDS
  calculate_damage  The exact name of the function you will write in
               this lesson. Your test looks for this name.
  attacker     The fighter doing the hitting. It has attack_power.
  defender     The fighter being hit. It has defense.
  defense      How much damage this fighter shrugs off.
  floor        A lowest allowed value. Here the floor is 1: however
               strong the armour, a hit always does at least 1.

HOW IT WORKS
  def calculate_damage(attacker, defender):
      damage = attacker.attack_power - defender.defense
      return max(damage, 1)

  The first line is the rule almost every RPG uses: how hard you hit,
  minus how well they are protected. With attack_power 12 against
  defense 4, that is 8 damage.

  But armour could make it zero or negative, so fights would never
  end. max(damage, 1) sets the floor: whichever is bigger, the
  calculated damage or 1. An attack of 3 against a defense of 10
  still lands for 1.

  Both parameters are whole objects, so the function reads
  attacker.attack_power and defender.defense with a dot.

YOUR TASK
  Step 1: Define a function named exactly calculate_damage that takes
          two parameters, attacker and defender.
  Step 2: Return attacker.attack_power minus defender.defense, but
          never less than 1.
  Step 3: Call calculate_damage with a strong attacker and a heavily
          armoured one, and print both results.

EXAMPLE
  This example is about a discount, so you still write your own
  damage formula.

      def final_price(item, voucher):
          price = item.price - voucher.amount
          return max(price, 1)

WHEN IT WORKS YOU'LL SEE
  Hero hits for 8 damage!
  Even against heavy armour, the blow lands for 1 damage.

IF YOU GET STUCK
  It returns 0 or a     -> wrap the result in max(damage, 1).
  negative number
  AttributeError        -> read attacker.attack_power and
                           defender.defense, with the dots.
  The test cannot find  -> the function must be named exactly
  your function            calculate_damage.

CHECK YOUR WORK
  python run_lesson.py 39
"""

# TODO: Write your code for Lesson 39 below this line.
