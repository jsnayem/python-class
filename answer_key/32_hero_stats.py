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


if __name__ == "__main__":
    hero = Hero("Alex")
    print(f"{hero.name}: {hero.health}/{hero.max_health} HP, alive={hero.is_alive()}")
    hero.health = 0
    print(f"After a hard fight: alive={hero.is_alive()}")
