"""Reference solution: Lesson 36 - Potion Class."""


class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value


class Potion(Item):
    def __init__(self, name, description, value, heal_amount):
        super().__init__(name, description, value)
        self.heal_amount = heal_amount


if __name__ == "__main__":
    potion = Potion("Health Potion", "Restores 30 HP", 20, 30)
    print(f"{potion.name}: heals {potion.heal_amount} HP for {potion.value} gold")
