"""Reference solution: Lesson 39 - Combat Loop (damage formula).

Damage is the attacker's attack power minus the defender's defense, with a
minimum of 1 so a hit always does something.
"""


def calculate_damage(attacker, defender):
    power = getattr(attacker, "attack_power", 10)
    defense = getattr(defender, "defense", 0)
    return max(1, power - defense)


if __name__ == "__main__":
    class _Fighter:
        def __init__(self, attack_power, defense):
            self.attack_power = attack_power
            self.defense = defense

    _hero = _Fighter(12, 2)
    _monster = _Fighter(8, 4)
    print(f"Hero hits for {calculate_damage(_hero, _monster)}")
    print(f"Monster hits for {calculate_damage(_monster, _hero)}")
