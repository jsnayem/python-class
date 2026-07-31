"""Reference solution: Lesson 37 - Monster Class."""


class Monster:
    def __init__(self, name, health, attack_power, gold_reward):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.gold_reward = gold_reward

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return damage
