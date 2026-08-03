"""Reference solution: Lesson 31 - Build the Hero Class."""

BASE_HEALTH = 100
BASE_GOLD = 50


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = BASE_HEALTH
        self.gold = BASE_GOLD


if __name__ == "__main__":
    hero = Hero("Alex")
    print(f"{hero.name}: {hero.health} HP, {hero.gold} gold")
