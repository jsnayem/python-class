"""
Lesson 38: The Combat System - Landing A Blow
==============================================

WHAT YOU'LL LEARN
  How to write a function where two objects meet: the hero swings,
  the monster takes the damage.

NEW WORDS
  attack(hero, monster)  The function you will write. It takes both
               objects so it can read one and change the other.
  equipped     The weapon a hero is currently holding. It may be
               None if they have nothing.
  None         Python's word for "nothing here".
  unarmed      A hero with no weapon. They still deal 1 damage.

HOW IT WORKS
  def attack(hero, monster):
      if hero.equipped_weapon is None:
          damage = 1
      else:
          damage = hero.equipped_weapon.attack_bonus
      monster.take_damage(damage)
      return damage

  Three jobs in order: work out the damage, apply it to the monster
  with the take_damage method from Lesson 37, and return the number
  so whoever called can print it.

  Checking for None matters. A brand new hero has no weapon, and
  reaching for .attack_bonus on nothing would crash the game. Giving
  them 1 damage keeps a bare-handed fight possible.

YOUR TASK
  Step 1: Define a function named attack that takes hero and monster.
  Step 2: Work out the damage: use the hero's weapon attack_bonus if
          they have one, otherwise 1 for an unarmed hero.
  Step 3: Call monster.take_damage(damage), then return damage.

EXAMPLE
  This example is a football kick, so you still write your own attack
  function.

      def kick(player, ball):
          power = 1 if player.boots is None else player.boots.power
          ball.move(power)
          return power

WHEN IT WORKS YOU'LL SEE
  Alex swings the Sword for 5 damage!
  The Goblin has 25 HP left.
  Bare-handed, Alex deals just 1 damage.

IF YOU GET STUCK
  AttributeError: None  -> check for None before reading
  has no attribute         .attack_bonus on the weapon.
  The monster's health  -> you must call monster.take_damage(damage),
  never changes            not just work the number out.
  attack returns None   -> add return damage as the last line.

CHECK YOUR WORK
  python run_lesson.py 38
"""

# TODO: Write your code for Lesson 38 below this line.
