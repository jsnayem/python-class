"""Reference solution: Lesson 35 - Weapon and Potion (subclasses of Item)."""


class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value


class Weapon(Item):
    def __init__(self, name, description, value, attack_bonus):
        super().__init__(name, description, value)
        self.attack_bonus = attack_bonus


class Potion(Item):
    def __init__(self, name, description, value, heal_amount):
        super().__init__(name, description, value)
        self.heal_amount = heal_amount
