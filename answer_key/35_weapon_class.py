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


if __name__ == "__main__":
    sword = Weapon("Sword", "A sharp blade", 50, 5)
    potion = Potion("Health Potion", "Restores HP", 20, 30)
    print(f"{sword.name}: +{sword.attack_bonus} attack, {sword.value} gold")
    print(f"{potion.name}: heals {potion.heal_amount}, {potion.value} gold")
