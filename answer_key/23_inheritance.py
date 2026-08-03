"""Reference solution: Lesson 23 - Inheritance (Shop Items).

Item is the base class; Weapon and Potion inherit from it and each calls
super().__init__() so the shared attributes (name, price) are set.
"""


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Weapon(Item):
    def __init__(self, name, price, bonus):
        super().__init__(name, price)
        self.bonus = bonus


class Potion(Item):
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount


if __name__ == "__main__":
    sword = Weapon("Sword", 50, 5)
    potion = Potion("Health Potion", 20, 30)
    print(f"{sword.name} costs {sword.price} gold (+{sword.bonus} attack)")
    print(f"{potion.name} costs {potion.price} gold (heals {potion.amount})")
