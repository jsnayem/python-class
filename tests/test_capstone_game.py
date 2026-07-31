"""Capstone integration test: the finished adventure game in main.py.

Exercises the real game classes/mechanics directly (no user input). Uses only
the standard library so it runs under run_lesson.py's own test runner as well
as pytest. main.py is imported once as a module; its __main__ guard means the
interactive game loop is NOT started on import.
"""
import importlib.util
import io
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).parent.parent
SPEC = importlib.util.spec_from_file_location("adventure_game", ROOT / "main.py")
game = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(game)


def test_constants():
    assert game.BASE_HEALTH == 100
    assert game.BASE_GOLD == 50


def test_hero_starts_alive_with_stats():
    hero = game.Hero("Alex")
    assert hero.name == "Alex"
    assert hero.health == 100 and hero.max_health == 100
    assert hero.gold == 50
    assert hero.is_alive() is True


def test_hero_take_damage_respects_defense_and_minimum():
    hero = game.Hero("Alex")
    hero.defense = 4
    dealt = hero.take_damage(10)
    assert dealt == 6
    assert hero.health == 94
    # minimum 1 damage even when defense exceeds attack
    hero.defense = 999
    dealt = hero.take_damage(3)
    assert dealt == 1


def test_hero_use_potion_heals_and_is_consumed():
    hero = game.Hero("Alex")
    hero.health = 50
    potion = game.Potion("Health Potion", "Restores 30 HP", 20, 30)
    hero.inventory.append(potion)
    hero.use_potion(potion)
    assert hero.health == 80
    assert potion not in hero.inventory


def test_monster_dies_and_gold_reward():
    monster = game.Monster("Goblin", 30, 8, 15)
    assert monster.is_alive() is True
    monster.take_damage(30)
    assert monster.is_alive() is False
    assert monster.health == 0


def test_create_monster_returns_fresh_instances():
    a = game.create_monster("goblin")
    b = game.create_monster("goblin")
    a.take_damage(10)
    assert a.health == 20
    assert b.health == 30  # independent, no shared mutation


def test_save_and_load_round_trip():
    import tempfile
    import os

    tmp = tempfile.mkdtemp()
    save_path = os.path.join(tmp, "savegame.json")
    with patch.object(game, "SAVE_FILE", save_path):
        hero = game.Hero("Zoe")
        hero.gold = 123
        hero.health = 70
        hero.inventory.append(game.Potion("Big Potion", "Restores 60 HP", 40, 60))
        game.save_game(hero)
        loaded = game.load_game()
    assert loaded is not None
    assert loaded.name == "Zoe"
    assert loaded.gold == 123
    assert loaded.health == 70
    assert any(isinstance(i, game.Potion) and i.heal_amount == 60 for i in loaded.inventory)


def test_combat_returns_victory_on_killing_blow():
    # Force a huge hero hit and feed "a" (attack) so combat never blocks on input.
    with patch.object(game.random, "randint", lambda a, b: 999), patch(
        "sys.stdin", io.StringIO("a\n")
    ):
        hero = game.Hero("Hero")
        monster = game.Monster("Rat", 5, 2, 5)
        result = game.combat(hero, monster)
    assert result == "victory"
    assert hero.gold == 50 + monster.gold_reward


def test_shop_buy_creates_new_item_instance():
    hero = game.Hero("Shopper")
    hero.gold = 100
    fake_input = io.StringIO("1\n1\n")
    before = len(hero.inventory)
    with patch("sys.stdin", fake_input):
        game.shop(hero)
    assert len(hero.inventory) == before + 1
    # bought item is a distinct instance from the shop template
    assert hero.inventory[-1] is not game.SHOP_ITEMS["sword"]
