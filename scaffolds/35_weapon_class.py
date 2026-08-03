"""
Lesson 35: Weapon And Potion - Two Kinds Of Item
=================================================

WHAT YOU'LL LEARN
  How to build two specific classes on top of Item, each adding one
  extra stat of its own.

NEW WORDS
  subclass     A class built on another. Weapon and Potion are
               subclasses of Item.
  super()      Means the parent class. super().__init__(...) runs
               Item's setup so you do not repeat it.
  attack_bonus The extra damage a Weapon adds.
  heal_amount  How much health a Potion restores.

HOW IT WORKS
  class Weapon(Item):
      def __init__(self, name, description, value, attack_bonus):
          super().__init__(name, description, value)
          self.attack_bonus = attack_bonus

  The super() line hands the first three values to Item, which stores
  name, description and value. Then Weapon stores the one extra thing
  it cares about. Potion follows exactly the same shape:

      class Potion(Item):
          def __init__(self, name, description, value, heal_amount):
              super().__init__(name, description, value)
              self.heal_amount = heal_amount

  Both are still Items, so they have every attribute Item gives them:

      sword = Weapon("Sword", "A blade", 50, 5)
      print(sword.name, sword.value, sword.attack_bonus)

YOUR TASK
  Step 1: Make sure the base class Item from Lesson 34 is defined at
          the top of your file.
  Step 2: Create a subclass named Weapon that adds attack_bonus, and
          a subclass named Potion that adds heal_amount. Both must
          call super().__init__(name, description, value) first.
  Step 3: Create one Weapon and one Potion, and print them both.

EXAMPLE
  This example is about tickets, so you still write your own Weapon
  and Potion.

      class Ticket:
          def __init__(self, event, price):
              self.event = event
              self.price = price

      class VipTicket(Ticket):
          def __init__(self, event, price, lounge):
              super().__init__(event, price)
              self.lounge = lounge

      v = VipTicket("Concert", 80, "Gold Room")
      print(v.event, v.price, v.lounge)

WHEN IT WORKS YOU'LL SEE
  Sword: A blade (50 gold, +5 attack)
  Health Potion: Heals you (20 gold, restores 30 health)

IF YOU GET STUCK
  NameError: Item is    -> define Item above Weapon and Potion.
  not defined
  AttributeError: no    -> you forgot super().__init__(...), so the
  attribute name           parent never stored the shared values.
  TypeError: missing    -> Weapon needs four arguments in order:
  argument                 name, description, value, attack_bonus.

CHECK YOUR WORK
  python run_lesson.py 35
"""

# TODO: Write your code for Lesson 35 below this line.
