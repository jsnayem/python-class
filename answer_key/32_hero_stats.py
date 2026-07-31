"""Reference solution: Lesson 32 - Hero Stats (Starting Bonuses)."""

BASE_HEALTH = 100
BASE_GOLD = 50


class Hero:
    def __init__(self, name):
        self.name = name
        self.max_health = BASE_HEALTH
        self.health = self.max_health
        self.gold = BASE_GOLD

    def is_alive(self):
        return self.health > 0
