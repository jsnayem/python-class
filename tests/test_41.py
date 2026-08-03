"""Tests for Lesson 41: Shop System - Buy Items."""
from _helpers import assert_scaffold_is_blank, defines_function, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(41)


def test_shop_has_prices():
    run = run_student(41)
    shop = run.get("shop")
    assert isinstance(shop, dict) and shop, "Step 1: create a shop dict of prices."
    assert all(isinstance(v, (int, float)) for v in shop.values()), (
        "Step 1: every shop entry needs a numeric price."
    )
    keys = {str(k).lower() for k in shop}
    assert "sword" in keys and "potion" in keys, (
        "Step 1: the shop should sell a sword and a potion."
    )


def test_defines_buy():
    assert defines_function(41, "buy"), "Step 2: define buy(hero, item_key)."


def test_buying_costs_gold_and_grants_the_item():
    run = run_student(41)
    hero = run.get("hero")
    assert hero is not None, "Step 3: create a hero."
    assert hero.gold < 50 or len(getattr(hero, "inventory", [])) >= 2, (
        "Step 3: after buying a sword and a potion the hero should have spent "
        "gold and gained items."
    )
