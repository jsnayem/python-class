"""Reference solution: Lesson 38 - Attack.

Deals damage equal to the hero's equipped weapon bonus (or 1 if unarmed)
and applies it to the monster. Reuses Monster.take_damage from lesson 37.
"""


def attack(hero, monster):
    weapon = getattr(hero, "weapon", None)
    bonus = getattr(weapon, "attack_bonus", 0)
    damage = bonus if bonus > 0 else 1
    monster.take_damage(damage)
    return damage


if __name__ == "__main__":
    class _Weapon:
        attack_bonus = 5

    class _Hero:
        weapon = _Weapon()

    class _Monster:
        name = "Goblin"
        health = 30

        def take_damage(self, damage):
            self.health -= damage

    _monster = _Monster()
    _dealt = attack(_Hero(), _monster)
    print(f"You hit the {_monster.name} for {_dealt} damage! ({_monster.health} HP left)")
