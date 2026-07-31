"""Reference solution: Lesson 39 - Combat Loop (damage formula).

Damage is the attacker's attack power minus the defender's defense, with a
minimum of 1 so a hit always does something.
"""


def calculate_damage(attacker, defender):
    power = getattr(attacker, "attack_power", 10)
    defense = getattr(defender, "defense", 0)
    return max(1, power - defense)
