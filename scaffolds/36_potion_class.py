"""
Lesson 36: The Potion Class - Healing Up
=========================================

WHAT YOU'LL LEARN
  How to focus on one subclass and give it a job to do, so your hero
  can drink a potion and get health back.

NEW WORDS
  heal_amount  How much health this potion restores.
  min()        A built-in that gives the smaller of two numbers. It
               is the neat way to stop healing past maximum.
  cap          To stop a number going above a limit. A hero on 95
               health drinking a 30-point potion should end on 100,
               not 125.

HOW IT WORKS
  class Potion(Item):
      def __init__(self, name, description, value, heal_amount):
          super().__init__(name, description, value)
          self.heal_amount = heal_amount

  A potion is an Item with one extra number. To make it useful, give
  it a method that acts on a hero:

      def use(self, hero):
          hero.health = min(hero.health + self.heal_amount,
                            hero.max_health)

  min() picks whichever is smaller: the healed total, or the hero's
  maximum. That single line caps the healing without needing an if.

YOUR TASK
  Step 1: Make sure Item is defined, then create a subclass named
          Potion that calls super().__init__(name, description,
          value) and stores heal_amount.
  Step 2: Give Potion a method named use that heals a hero without
          letting their health go above max_health.
  Step 3: Create a Health Potion, print it, and use it on a wounded
          hero to show the healing working.

EXAMPLE
  This example is a phone charger, so you still write your own
  Potion.

      class Charger:
          def __init__(self, power):
              self.power = power

          def use(self, phone):
              phone.battery = min(phone.battery + self.power, 100)

WHEN IT WORKS YOU'LL SEE
  Health Potion: Restores HP (20 gold, heals 30)
  Alex drinks it. Health goes from 70 to 100!

IF YOU GET STUCK
  Health goes over     -> use min(...) with hero.max_health, or the
  maximum                 hero will overheal.
  AttributeError:      -> the hero needs max_health from Lesson 32.
  max_health
  TypeError: missing   -> Potion takes four arguments: name,
  argument                description, value, heal_amount.

CHECK YOUR WORK
  python run_lesson.py 36
"""

# TODO: Write your code for Lesson 36 below this line.
