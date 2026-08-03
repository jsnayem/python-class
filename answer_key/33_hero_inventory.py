"""Reference solution: Lesson 33 - Hero Inventory."""


class Hero:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)


if __name__ == "__main__":
    hero = Hero("Alex")
    hero.add_item("sword")
    print(f"{hero.name} carries: {hero.inventory}")
    hero.drop_item("sword")
    print(f"After dropping the sword: {hero.inventory}")
