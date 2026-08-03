"""
Lesson 41: The Shop - Spending Your Gold
=========================================

WHAT YOU'LL LEARN
  How to build a shop with a price list, and a buy function that
  checks the hero can afford something before selling it.

NEW WORDS
  shop         A dictionary of prices, where each key is an item name
               and each value is what it costs.
  item_key     The name used to look an item up in the shop, such as
               "sword" or "potion".
  in           Asks whether a key exists in a dictionary. Always
               check before looking something up.
  afford       Whether the hero has enough gold for the price.

HOW IT WORKS
  shop = {"sword": 30, "potion": 10}

  A dictionary is perfect here: you look a price up by name instead
  of remembering positions. Now the buying rules:

      def buy(hero, item_key):
          if item_key not in shop:
              print("We don't sell that.")
              return False
          price = shop[item_key]
          if hero.gold < price:
              print("You cannot afford that!")
              return False
          hero.gold = hero.gold - price
          hero.inventory.append(item_key)
          return True

  Notice the order. Check the item exists, then check the gold, and
  only then take payment and hand over the goods. Real shop code
  works exactly like this: refuse early, act last.

YOUR TASK
  Step 1: Create a dictionary named shop with at least the keys
          "sword" and "potion", each with a number price.
  Step 2: Define a function named buy that takes hero and item_key,
          refuses when the item is unknown or the hero is too poor,
          and otherwise subtracts the price and adds the item to the
          hero's inventory.
  Step 3: Create a variable named hero using your Hero class, then
          buy a sword and a potion so the hero spends gold and gains
          both items.

EXAMPLE
  This example is a cafe, so you still write your own shop.

      menu = {"tea": 2, "cake": 5}

      def order(customer, item):
          if item not in menu:
              return False
          if customer.coins < menu[item]:
              return False
          customer.coins -= menu[item]
          return True

WHEN IT WORKS YOU'LL SEE
  Welcome to the shop! sword: 30 gold, potion: 10 gold
  Alex buys a sword. Gold left: 20
  Alex buys a potion. Gold left: 10

IF YOU GET STUCK
  KeyError             -> check the key is in the shop before using
                          shop[item_key].
  Gold never drops     -> store it back: hero.gold = hero.gold - price
  AttributeError:      -> your hero needs the inventory list from
  inventory               Lesson 33.

CHECK YOUR WORK
  python run_lesson.py 41
"""

# TODO: Write your code for Lesson 41 below this line.
