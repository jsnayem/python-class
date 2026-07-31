"""
ELABORATE ADVENTURE GAME
------------------------
A text-based RPG that demonstrates:
- Variables & Data Types
- Lists, Tuples, Dictionaries
- Conditionals & Loops
- Functions (with defaults, docstrings, *args)
- Classes & Objects
- Error Handling (try/except)
- File I/O (save/load)
- Randomness & Timing
- F-strings and formatting
- ANSI Color codes and terminal decoration
- The if __name__ == "__main__" guard
"""

import json
import random
import sys
import time
from typing import Optional

# ============================
# CONSTANTS (magic numbers extracted)
# ============================

BASE_HEALTH = 100
BASE_GOLD = 50
STARTING_GOLD_BONUS = 10
TOWN_REST_HEAL = 5
FLEE_SUCCESS_CHANCE = 0.5
RANDOM_ENCOUNTER_CHANCE = 0.2
LOOT_DROP_CHANCE = 0.3
MIN_DAMAGE = 1
BASE_ATTACK = 10
SAVE_FILE = "savegame.json"

# Tuple of valid action choices in combat (demonstrates tuples)
COMBAT_ACTIONS = ("a", "u", "f")

# Tuple of valid random encounter monsters
RANDOM_ENCOUNTER_MONSTERS = ("goblin", "orc")


# ============================
# COLOR SYSTEM (ANSI escape codes)
# ============================

class Color:
    """ANSI color codes for terminal text decoration.

    Demonstrates: class attributes, string constants, and a helper method.
    Usage: print(f"{Color.RED}Error!{Color.RESET}")
    """

    # Foreground colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    # Background colors
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"

    # Text styles
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"

    # Reset
    RESET = "\033[0m"

    @staticmethod
    def colorize(text: str, color: str) -> str:
        """Wrap text in a color code and reset."""
        return f"{color}{text}{Color.RESET}"


def print_header(title: str) -> None:
    """Print a decorative header with colored borders."""
    width = 50
    border = "=" * width
    print(f"\n{Color.BRIGHT_CYAN}{Color.BOLD}{border}{Color.RESET}")
    print(f"{Color.BRIGHT_CYAN}{Color.BOLD}{title.center(width)}{Color.RESET}")
    print(f"{Color.BRIGHT_CYAN}{Color.BOLD}{border}{Color.RESET}")


def print_success(text: str) -> None:
    """Print success message in green."""
    print(f"{Color.BRIGHT_GREEN}{text}{Color.RESET}")


def print_error(text: str) -> None:
    """Print error message in red."""
    print(f"{Color.BRIGHT_RED}{text}{Color.RESET}")


def print_warning(text: str) -> None:
    """Print warning message in yellow."""
    print(f"{Color.BRIGHT_YELLOW}{text}{Color.RESET}")


def print_info(text: str) -> None:
    """Print info message in cyan."""
    print(f"{Color.BRIGHT_CYAN}{text}{Color.RESET}")


# ============================
# 1. CLASSES (OOP)
# ============================

class Item:
    """Base class for all items."""

    def __init__(self, name: str, description: str, value: int):
        self.name = name
        self.description = description
        self.value = value  # gold value or healing amount, etc.

    def __str__(self) -> str:
        return f"{self.name} ({self.description})"

    def __repr__(self) -> str:
        return f"Item(name={self.name!r}, description={self.description!r}, value={self.value})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Item):
            return NotImplemented
        return (
            type(self) == type(other)
            and self.name == other.name
            and self.description == other.description
            and self.value == other.value
            and getattr(self, "attack_bonus", None) == getattr(other, "attack_bonus", None)
            and getattr(self, "heal_amount", None) == getattr(other, "heal_amount", None)
        )

    def __hash__(self) -> int:
        return hash((type(self).__name__, self.name, self.description, self.value))


class Weapon(Item):
    """Weapon that increases attack power."""

    def __init__(self, name: str, description: str, value: int, attack_bonus: int):
        super().__init__(name, description, value)
        self.attack_bonus = attack_bonus

    def __repr__(self) -> str:
        return (
            f"Weapon(name={self.name!r}, description={self.description!r}, "
            f"value={self.value}, attack_bonus={self.attack_bonus})"
        )


class Potion(Item):
    """Potion that heals the hero."""

    def __init__(self, name: str, description: str, value: int, heal_amount: int):
        super().__init__(name, description, value)
        self.heal_amount = heal_amount

    def __repr__(self) -> str:
        return (
            f"Potion(name={self.name!r}, description={self.description!r}, "
            f"value={self.value}, heal_amount={self.heal_amount})"
        )


class Hero:
    """The player's character."""

    def __init__(self, name: str):
        self.name = name
        self.max_health = BASE_HEALTH
        self.health = self.max_health
        self.gold = BASE_GOLD
        self.inventory: list[Item] = []  # list of Item objects
        self.weapon: Optional[Weapon] = None  # currently equipped Weapon
        self.defense = 0  # simple armor (reduces damage)

    def is_alive(self) -> bool:
        return self.health > 0

    def equip_weapon(self, weapon: Weapon) -> None:
        """Equip a weapon from inventory."""
        if weapon in self.inventory and isinstance(weapon, Weapon):
            self.weapon = weapon
            print_success(f"Equipped {weapon.name}.")
        else:
            print_error("You don't have that weapon.")

    def use_potion(self, potion: Potion) -> None:
        """Consume a potion from inventory."""
        if potion in self.inventory and isinstance(potion, Potion):
            self.health = min(self.max_health, self.health + potion.heal_amount)
            self.inventory.remove(potion)
            print_success(f"Used {potion.name}. Health is now {self.health}.")
        else:
            print_error("You don't have that potion.")

    def attack_power(self) -> int:
        """Total attack = base + weapon bonus."""
        base = BASE_ATTACK
        bonus = self.weapon.attack_bonus if self.weapon else 0
        return base + bonus

    def take_damage(self, damage: int) -> int:
        """Reduce health by damage minus defense."""
        actual = max(MIN_DAMAGE, damage - self.defense)  # minimum 1 damage
        self.health -= actual
        if self.health < 0:
            self.health = 0
        return actual

    def __str__(self) -> str:
        weapon_name = self.weapon.name if self.weapon else "Fists"
        # Color health based on percentage
        health_pct = self.health / self.max_health
        if health_pct > 0.5:
            hp_color = Color.BRIGHT_GREEN
        elif health_pct > 0.2:
            hp_color = Color.BRIGHT_YELLOW
        else:
            hp_color = Color.BRIGHT_RED
        return (
            f"{Color.BRIGHT_YELLOW}⚔️ {self.name}{Color.RESET} | "
            f"{hp_color}HP: {self.health}/{self.max_health}{Color.RESET} | "
            f"{Color.BRIGHT_YELLOW}Gold: {self.gold}{Color.RESET} | "
            f"Weapon: {weapon_name} | Defense: {self.defense}"
        )

    def __repr__(self) -> str:
        return (
            f"Hero(name={self.name!r}, health={self.health}, "
            f"max_health={self.max_health}, gold={self.gold}, "
            f"weapon={self.weapon!r}, defense={self.defense})"
        )


class Monster:
    """Enemy that the hero fights."""

    def __init__(
        self,
        name: str,
        health: int,
        attack_power: int,
        gold_reward: int,
        description: str = "",
    ):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.gold_reward = gold_reward
        self.description = description

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, damage: int) -> int:
        """Reduce health by damage. Returns actual damage dealt."""
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return damage

    def __str__(self) -> str:
        health_pct = self.health / self.max_health
        if health_pct > 0.5:
            hp_color = Color.BRIGHT_GREEN
        elif health_pct > 0.2:
            hp_color = Color.BRIGHT_YELLOW
        else:
            hp_color = Color.BRIGHT_RED
        return (
            f"{Color.BRIGHT_RED}{self.name}{Color.RESET} "
            f"({hp_color}HP: {self.health}/{self.max_health}{Color.RESET})"
        )

    def __repr__(self) -> str:
        return (
            f"Monster(name={self.name!r}, health={self.health}, "
            f"max_health={self.max_health}, attack_power={self.attack_power}, "
            f"gold_reward={self.gold_reward}, description={self.description!r})"
        )


# ============================
# 2. GAME DATA (Dictionaries & Lists)
# ============================

# Predefined monsters with different difficulty.
# These are templates; fresh Monster instances are created for each encounter
# (see create_monster() below) to avoid mutating shared state.
MONSTER_TEMPLATES = {
    "goblin": {
        "name": "Goblin",
        "health": 30,
        "attack_power": 8,
        "gold_reward": 15,
        "description": "A small, green, greedy creature.",
    },
    "orc": {
        "name": "Orc",
        "health": 50,
        "attack_power": 12,
        "gold_reward": 30,
        "description": "A brutish humanoid with a big axe.",
    },
    "troll": {
        "name": "Troll",
        "health": 70,
        "attack_power": 15,
        "gold_reward": 50,
        "description": "A massive, regenerating beast.",
    },
    "dragon": {
        "name": "Dragon",
        "health": 120,
        "attack_power": 25,
        "gold_reward": 100,
        "description": "A fearsome fire-breathing wyrm.",
    },
}


def create_monster(key: str) -> Monster:
    """Create a fresh Monster instance from a template key.

    This avoids the shared-mutation bug where modifying a Monster in the
    MONSTER_TEMPLATES dict would affect all references.
    """
    template = MONSTER_TEMPLATES[key]
    return Monster(
        template["name"],
        template["health"],
        template["attack_power"],
        template["gold_reward"],
        template["description"],
    )


# Available items in the shop
SHOP_ITEMS = {
    "health_potion": Potion("Health Potion", "Restores 30 HP", 20, 30),
    "great_potion": Potion("Great Potion", "Restores 60 HP", 40, 60),
    "sword": Weapon("Iron Sword", "A sturdy blade (+5 attack)", 50, 5),
    "axe": Weapon("Battle Axe", "Heavy and brutal (+10 attack)", 80, 10),
}

# World map: locations with descriptions and possible monsters.
# Built fresh by new_game() so monster assignments vary each playthrough
# (random.choice runs at game start, not at import time).
def new_game():
    """Create a fresh WORLD map with randomized monster encounters."""
    return {
        "town": {
            "desc": "You are in a safe village. There's a shop and a well.",
            "monster": None,
            "exits": {"north": "forest", "east": "cave"},
        },
        "forest": {
            "desc": "Dense, dark woods. You hear rustling.",
            "monster": random.choice(["goblin", "orc"]),
            "exits": {"south": "town", "east": "dungeon"},
        },
        "cave": {
            "desc": "A damp, echoing cavern. Stalactites drip water.",
            "monster": random.choice(["orc", "troll"]),
            "exits": {"west": "town", "north": "dungeon"},
        },
        "dungeon": {
            "desc": "The lair of the Dragon! The air is hot and smoky.",
            "monster": "dragon",
            "exits": {"south": "forest", "west": "cave"},
        },
    }


# ============================
# 3. FUNCTIONS (with docstrings, defaults, and *args)
# ============================

def display_status(hero: Hero, location: str) -> None:
    """Print the hero's stats and current location."""
    print_header(f"{Color.BRIGHT_YELLOW}📍 {location.upper()}{Color.RESET}")
    print(hero)
    print(f"{Color.BRIGHT_CYAN}📍 Location: {location.upper()}{Color.RESET} - {WORLD[location]['desc']}")
    print(f"{Color.BRIGHT_CYAN}{'=' * 50}{Color.RESET}")


def show_inventory(hero: Hero) -> None:
    """Display all items in hero's inventory with indices."""
    if not hero.inventory:
        print_warning("Your inventory is empty.")
        return
    print(f"\n{Color.BRIGHT_YELLOW}🎒 INVENTORY:{Color.RESET}")
    for idx, item in enumerate(hero.inventory, 1):
        # Color items by type
        if isinstance(item, Weapon):
            item_str = f"{Color.BRIGHT_BLUE}{item}{Color.RESET}"
        elif isinstance(item, Potion):
            item_str = f"{Color.BRIGHT_GREEN}{item}{Color.RESET}"
        else:
            item_str = str(item)
        print(f"  {Color.BRIGHT_CYAN}{idx}.{Color.RESET} {item_str}")
    print()


def show_objectives() -> None:
    """Display the player's current objectives."""
    print(f"\n{Color.BRIGHT_MAGENTA}📜 OBJECTIVES:{Color.RESET}")
    print(f"  {Color.BRIGHT_CYAN}1.{Color.RESET} Explore the world (forest, cave, dungeon)")
    print(f"  {Color.BRIGHT_CYAN}2.{Color.RESET} Defeat monsters to gain gold and loot")
    print(f"  {Color.BRIGHT_CYAN}3.{Color.RESET} Defeat the {Color.BRIGHT_RED}Dragon{Color.RESET} in the Dungeon to save the kingdom!")
    print()


def combat(hero: Hero, monster: Monster) -> str:
    """
    Handle turn-based combat between hero and monster.

    Returns:
        "victory" if hero wins,
        "defeat" if hero dies,
        "fled" if hero successfully flees,
        "flee_failed" if hero failed to flee (combat continues).
    """
    print(f"\n{Color.BRIGHT_RED}⚔️ A wild {monster.name} appears! {Color.RESET}{monster.description}")
    time.sleep(1)

    while hero.is_alive() and monster.is_alive():
        # Hero's turn
        print(f"\n{Color.BRIGHT_GREEN}Your HP: {hero.health}{Color.RESET} | "
              f"{Color.BRIGHT_RED}{monster.name} HP: {monster.health}{Color.RESET}")
        action = input(f"{Color.BRIGHT_YELLOW}(A)ttack, (U)se potion, (F)lee? {Color.RESET}").lower().strip()

        if action == "a":
            # Attack
            damage = random.randint(5, hero.attack_power())
            monster.take_damage(damage)
            print(f"{Color.BRIGHT_GREEN}You strike {monster.name} for {damage} damage!{Color.RESET}")
            time.sleep(0.5)

        elif action == "u":
            # Use a potion – pick from inventory
            potions = [item for item in hero.inventory if isinstance(item, Potion)]
            if not potions:
                print_warning("You have no potions!")
                continue
            print(f"{Color.BRIGHT_YELLOW}Choose a potion:{Color.RESET}")
            for i, pot in enumerate(potions, 1):
                print(f"  {Color.BRIGHT_GREEN}{i}.{Color.RESET} {pot} (heals {pot.heal_amount})")
            try:
                choice = int(input(f"{Color.BRIGHT_CYAN}> {Color.RESET}")) - 1
                if 0 <= choice < len(potions):
                    hero.use_potion(potions[choice])
                else:
                    print_error("Invalid choice.")
            except ValueError:
                print_error("Enter a number.")
            continue  # Skip monster's turn after using item

        elif action == "f":
            # Flee: 50% chance
            if random.random() < FLEE_SUCCESS_CHANCE:
                print_success("You fled successfully!")
                return "fled"
            else:
                print_warning("You failed to flee!")
                # Combat continues — monster gets a turn

        else:
            print_error(f"Invalid action. Choose from {COMBAT_ACTIONS}.")
            continue

        # Check if monster is dead after hero's attack
        if not monster.is_alive():
            print_success(f"\n🎉 You defeated the {monster.name}!")
            gold_won = monster.gold_reward
            hero.gold += gold_won
            print(f"{Color.BRIGHT_YELLOW}You found {gold_won} gold.{Color.RESET}")
            # Drop random loot (maybe a potion or weapon)
            if random.random() < LOOT_DROP_CHANCE:
                loot = random.choice(list(SHOP_ITEMS.values()))
                hero.inventory.append(loot)
                print(f"{Color.BRIGHT_MAGENTA}The monster dropped a {loot.name}!{Color.RESET}")
            return "victory"

        # Monster's turn (only if hero is alive)
        if hero.is_alive():
            damage = random.randint(5, monster.attack_power)
            actual = hero.take_damage(damage)
            print(f"{Color.BRIGHT_RED}{monster.name} hits you for {actual} damage!{Color.RESET}")
            time.sleep(0.5)

    # Loop ends if hero dies
    if not hero.is_alive():
        print_error(f"\n💀 You have been slain by the {monster.name}...")
        return "defeat"


def shop(hero: Hero) -> None:
    """Interact with the shopkeeper to buy/sell items."""
    print(f"\n{Color.BRIGHT_YELLOW}🏪 Welcome to the shop!{Color.RESET}")
    print(f"Your gold: {Color.BRIGHT_YELLOW}{hero.gold}{Color.RESET}")
    print(f"{Color.BRIGHT_CYAN}What would you like to do?{Color.RESET}")
    print(f"  {Color.BRIGHT_GREEN}1.{Color.RESET} Buy items")
    print(f"  {Color.BRIGHT_GREEN}2.{Color.RESET} Sell items")
    print(f"  {Color.BRIGHT_GREEN}3.{Color.RESET} Leave")
    choice = input(f"{Color.BRIGHT_CYAN}> {Color.RESET}").strip()

    if choice == "1":
        # Display items for sale
        items_list = list(SHOP_ITEMS.values())
        print(f"\n{Color.BRIGHT_YELLOW}Items for sale:{Color.RESET}")
        for idx, item in enumerate(items_list, 1):
            if isinstance(item, Weapon):
                item_color = Color.BRIGHT_BLUE
            elif isinstance(item, Potion):
                item_color = Color.BRIGHT_GREEN
            else:
                item_color = Color.RESET
            print(f"  {Color.BRIGHT_CYAN}{idx}.{Color.RESET} {item_color}{item.name}{Color.RESET} - {item.value} gold")
        try:
            pick = int(input(f"{Color.BRIGHT_CYAN}Enter item number to buy (or 0 to cancel): {Color.RESET}")) - 1
            if pick == -1:
                return
            if 0 <= pick < len(items_list):
                item = items_list[pick]
                if hero.gold >= item.value:
                    hero.gold -= item.value
                    # Create a new instance to avoid sharing references
                    if isinstance(item, Weapon):
                        new_item = Weapon(
                            item.name, item.description, item.value, item.attack_bonus
                        )
                    elif isinstance(item, Potion):
                        new_item = Potion(
                            item.name, item.description, item.value, item.heal_amount
                        )
                    else:
                        new_item = Item(item.name, item.description, item.value)
                    hero.inventory.append(new_item)
                    print_success(f"Bought {item.name}.")
                else:
                    print_error("Not enough gold!")
            else:
                print_error("Invalid number.")
        except ValueError:
            print_error("Please enter a number.")

    elif choice == "2":
        # Sell items (half price)
        if not hero.inventory:
            print_warning("You have nothing to sell.")
            return
        show_inventory(hero)
        try:
            idx = int(input(f"{Color.BRIGHT_CYAN}Enter item number to sell (or 0 to cancel): {Color.RESET}")) - 1
            if idx == -1:
                return
            if 0 <= idx < len(hero.inventory):
                item = hero.inventory.pop(idx)
                sell_price = item.value // 2
                hero.gold += sell_price
                print_success(f"Sold {item.name} for {sell_price} gold.")
            else:
                print_error("Invalid number.")
        except ValueError:
            print_error("Enter a number.")
    elif choice == "3":
        print("Goodbye!")
    else:
        print_error("Invalid choice.")


def save_game(hero: Hero) -> None:
    """Save hero stats to a JSON file.

    Uses JSON format for robustness: handles special characters in names,
    preserves all item types, and is human-readable/editable.
    """
    try:
        # Build a serializable dict
        save_data = {
            "name": hero.name,
            "health": hero.health,
            "max_health": hero.max_health,
            "gold": hero.gold,
            "defense": hero.defense,
            "inventory": [
                {
                    "type": type(item).__name__,
                    "name": item.name,
                    "description": item.description,
                    "value": item.value,
                    "attack_bonus": getattr(item, "attack_bonus", None),
                    "heal_amount": getattr(item, "heal_amount", None),
                }
                for item in hero.inventory
            ],
            "weapon": hero.weapon.name if hero.weapon else None,
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(save_data, f, indent=2)
        print_success("Game saved!")
    except (IOError, OSError, TypeError) as e:
        print_error(f"Save failed: {e}")


def load_game() -> Optional[Hero]:
    """Load hero from save file. Returns a Hero object or None."""
    try:
        with open(SAVE_FILE, "r") as f:
            save_data = json.load(f)

        name = save_data["name"]
        health = int(save_data["health"])
        max_health = int(save_data["max_health"])
        gold = int(save_data["gold"])
        defense = int(save_data["defense"])

        hero = Hero(name)
        hero.health = health
        hero.max_health = max_health
        hero.gold = gold
        hero.defense = defense

        # Parse inventory — reconstruct full Item objects from saved data
        for item_data in save_data.get("inventory", []):
            class_name = item_data["type"]
            item_name = item_data["name"]
            item_desc = item_data["description"]
            item_value = item_data["value"]
            attack_bonus = item_data.get("attack_bonus")
            heal_amount = item_data.get("heal_amount")

            if class_name == "Weapon" and attack_bonus is not None:
                new_item = Weapon(item_name, item_desc, item_value, attack_bonus)
            elif class_name == "Potion" and heal_amount is not None:
                new_item = Potion(item_name, item_desc, item_value, heal_amount)
            else:
                new_item = Item(item_name, item_desc, item_value)
            hero.inventory.append(new_item)

        # Equip weapon if saved
        weapon_name = save_data.get("weapon")
        if weapon_name:
            for item in hero.inventory:
                if isinstance(item, Weapon) and item.name == weapon_name:
                    hero.equip_weapon(item)
                    break

        print_success("Game loaded successfully!")
        return hero
    except FileNotFoundError:
        print_warning("No save file found.")
        return None
    except (json.JSONDecodeError, KeyError, ValueError, TypeError) as e:
        print_error(f"Load failed: corrupted save file ({e}).")
        return None


# ============================
# 4. MAIN GAME LOOP (The core)
# ============================

def main() -> None:
    """The main entry point of the game."""
    print(f"{Color.BRIGHT_YELLOW}{Color.BOLD}🐉 WELCOME TO THE ADVENTURE GAME!{Color.RESET}")
    print(f"{Color.BRIGHT_CYAN}You are a brave hero in a fantasy world.{Color.RESET}\n")

    # Load or create hero
    load_choice = input(f"{Color.BRIGHT_CYAN}Load saved game? (y/n): {Color.RESET}").lower().strip()
    if load_choice == "y":
        hero = load_game()
        if hero is None:
            print_warning("Starting a new game instead.")
            # strip() removes whitespace; `or "Hero"` provides a default
            # if the user enters only spaces or presses Enter
            hero = Hero(input(f"{Color.BRIGHT_CYAN}Enter your hero's name: {Color.RESET}").strip() or "Hero")
    else:
        hero = Hero(input(f"{Color.BRIGHT_CYAN}Enter your hero's name: {Color.RESET}").strip() or "Hero")

    # Give starting items
    if not hero.inventory:  # only if fresh start
        hero.inventory.append(Potion("Health Potion", "Restores 30 HP", 20, 30))
        hero.gold += STARTING_GOLD_BONUS

    current_location = "town"
    game_over = False
    quit_game = False
    WORLD = new_game()

    # ===== MAIN GAME LOOP =====
    while not game_over and hero.is_alive() and not quit_game:
        display_status(hero, current_location)
        show_objectives()

        # Check if there's a monster in this location
        monster_key = WORLD[current_location]["monster"]
        monster = None
        if monster_key and monster_key in MONSTER_TEMPLATES:
            # Create a fresh monster instance (so each encounter is new)
            monster = create_monster(monster_key)

        # Show available actions
        print(f"\n{Color.BRIGHT_CYAN}What do you want to do?{Color.RESET}")
        print(f"  {Color.BRIGHT_GREEN}(m){Color.RESET} Move to another location")
        if monster:
            print(f"  {Color.BRIGHT_RED}(f){Color.RESET} Fight the monster here")
        if current_location == "town":
            print(f"  {Color.BRIGHT_YELLOW}(s){Color.RESET} Visit the shop")
        print(f"  {Color.BRIGHT_BLUE}(i){Color.RESET} Show inventory")
        print(f"  {Color.BRIGHT_BLUE}(e){Color.RESET} Equip a weapon")
        print(f"  {Color.BRIGHT_GREEN}(u){Color.RESET} Use a potion")
        print(f"  {Color.BRIGHT_MAGENTA}(v){Color.RESET} Save game")
        print(f"  {Color.BRIGHT_BLACK}(q){Color.RESET} Quit game")

        action = input(f"{Color.BRIGHT_CYAN}> {Color.RESET}").lower().strip()

        # ----- Action handling -----
        if action == "m":
            # Show exits
            exits = WORLD[current_location]["exits"]
            print(f"{Color.BRIGHT_CYAN}Exits:{Color.RESET} {', '.join(exits.keys())}")
            dest = input(f"{Color.BRIGHT_CYAN}Where to? {Color.RESET}").strip().lower()
            if dest in exits:
                current_location = exits[dest]
                print(f"{Color.BRIGHT_GREEN}You travel to {current_location}.{Color.RESET}")
                # Random encounter chance when moving (extra)
                if random.random() < RANDOM_ENCOUNTER_CHANCE and current_location != "town":
                    print_warning("On the way, you encounter a random monster!")
                    # Pick a random weak monster from the tuple
                    rand_monster_key = random.choice(RANDOM_ENCOUNTER_MONSTERS)
                    mob = create_monster(rand_monster_key)
                    result = combat(hero, mob)
                    if result == "defeat":
                        game_over = True
                        break
                    elif result == "fled":
                        print_info("You continue on your journey...")
                    # "victory" or "flee_failed" → continue normally
            else:
                print_error("You can't go there.")

        elif action == "f" and monster:
            # Fight the monster
            result = combat(hero, monster)
            if result == "victory":
                # After victory, remove monster from location permanently
                WORLD[current_location]["monster"] = None
                print_success("The area is now clear.")
            elif result == "defeat":
                game_over = True
                break
            elif result == "fled":
                print_info("You escaped from the area...")
            # "flee_failed" → combat already handled, loop continues

        elif action == "s" and current_location == "town":
            shop(hero)

        elif action == "i":
            show_inventory(hero)

        elif action == "e":
            # Equip a weapon from inventory
            weapons = [item for item in hero.inventory if isinstance(item, Weapon)]
            if not weapons:
                print_warning("You have no weapons to equip.")
            else:
                print(f"{Color.BRIGHT_YELLOW}Select a weapon to equip:{Color.RESET}")
                for idx, w in enumerate(weapons, 1):
                    print(f"  {Color.BRIGHT_BLUE}{idx}.{Color.RESET} {w.name} (atk +{w.attack_bonus})")
                try:
                    ch = int(input(f"{Color.BRIGHT_CYAN}> {Color.RESET}")) - 1
                    if 0 <= ch < len(weapons):
                        hero.equip_weapon(weapons[ch])
                    else:
                        print_error("Invalid.")
                except ValueError:
                    print_error("Enter a number.")

        elif action == "u":
            potions = [item for item in hero.inventory if isinstance(item, Potion)]
            if not potions:
                print_warning("You have no potions.")
            else:
                print(f"{Color.BRIGHT_GREEN}Select a potion to use:{Color.RESET}")
                for idx, p in enumerate(potions, 1):
                    print(f"  {Color.BRIGHT_GREEN}{idx}.{Color.RESET} {p.name} (heals {p.heal_amount})")
                try:
                    ch = int(input(f"{Color.BRIGHT_CYAN}> {Color.RESET}")) - 1
                    if 0 <= ch < len(potions):
                        hero.use_potion(potions[ch])
                    else:
                        print_error("Invalid.")
                except ValueError:
                    print_error("Enter a number.")

        elif action == "v":
            save_game(hero)

        elif action == "q":
            print_success("Thanks for playing! Goodbye.")
            quit_game = True

        else:
            print_error("Invalid action. Try again.")

        # Automatically heal a little when in town (rest)
        # This happens AFTER action processing so quit doesn't skip it
        if current_location == "town" and hero.health < hero.max_health:
            hero.health = min(hero.max_health, hero.health + TOWN_REST_HEAL)
            print(f"{Color.BRIGHT_GREEN}You rest in town and recover {TOWN_REST_HEAL} HP.{Color.RESET}")

        # Check if hero has finished (e.g., defeated dragon)
        if WORLD["dungeon"]["monster"] is None and current_location == "dungeon":
            print_success("\n🌟 YOU HAVE DEFEATED THE DRAGON AND SAVED THE KINGDOM!")
            print(f"{Color.BRIGHT_YELLOW}Congratulations! You won!{Color.RESET}")
            game_over = True

    # End game
    if not hero.is_alive():
        print_error("\n💀 GAME OVER")
    elif game_over:
        print_success("\n🏆 Thanks for playing!")


# ============================
# 5. STANDARD GUARD
# ============================
if __name__ == "__main__":
    main()
