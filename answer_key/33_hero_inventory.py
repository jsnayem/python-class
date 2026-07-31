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
