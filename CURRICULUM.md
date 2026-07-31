# 50-Lesson Python Adventure Game Curriculum

## Overview

A scaffolded curriculum where an 11-year-old student builds a complete text-based RPG across 50 bite-sized lessons. Each lesson is 15-30 minutes, introduces one Python concept, includes auto-tests, and adds a piece to the growing game. The student starts with "Hello, World!" and ends with a polished, colored, saveable RPG.

## Directory Structure

```
python-class/
├── lessons/
│   ├── 01_hello_world.py
│   ├── 02_variables.py
│   ├── 03_printing.py
│   ├── 04_math.py
│   ├── 05_strings.py
│   ├── 06_input.py
│   ├── 07_if_statements.py
│   ├── 08_if_statements.py
│   ├── 09_lists.py
│   ├── 10_functions.py
│   ├── 11_loops_intro.py
│   ├── 12_while_loops.py
│   ├── 13_for_loops.py
│   ├── 14_functions_intro.py
│   ├── 15_function_args.py
│   ├── 16_return_values.py
│   ├── 17_dictionaries.py
│   ├── 18_tuples.py
│   ├── 19_classes_intro.py
│   ├── 20_objects.py
│   ├── 21_attributes.py
│   ├── 22_methods.py
│   ├── 23_inheritance.py
│   ├── 24_try_except.py
│   ├── 25_file_writing.py
│   ├── 26_file_reading.py
│   ├── 27_json.py
│   ├── 28_random.py
│   ├── 29_time.py
│   ├── 30_f_strings.py
│   ├── 31_hero_class.py
│   ├── 32_hero_stats.py
│   ├── 33_hero_inventory.py
│   ├── 34_item_class.py
│   ├── 35_weapon_class.py
│   ├── 36_potion_class.py
│   ├── 37_monster_class.py
│   ├── 38_combat_system.py
│   ├── 39_attack_logic.py
│   ├── 40_flee_mechanic.py
│   ├── 41_shop_system.py
│   ├── 42_world_map.py
│   ├── 43_game_loop.py
│   ├── 44_save_system.py
│   ├── 45_load_system.py
│   ├── 46_color_system.py
│   ├── 47_decorative_ui.py
│   ├── 48_objectives.py
│   ├── 49_final_integration.py
│   └── 50_play_and_share.py
├── tests/
│   ├── test_01.py
│   ├── test_02.py
│   └── ... (one per lesson)
├── scaffolds/
│   └── (partial code templates per lesson)
├── run_lesson.py
├── progress.json
└── README.md
```

## Phase Breakdown

### Phase 1: Python Fundamentals (Lessons 1-30)

**Goal**: Learn core Python syntax through mini-games and puzzles

| Lessons | Concepts | Mini-Projects |
|---------|----------|---------------|
| 1-6 | Hello World, variables, printing, math, strings, input | Magic 8-Ball, Number Guesser |
| 7-13 | Conditionals, comparisons, lists, loops | Text adventure with 3 rooms, Quiz game |
| 14-18 | Functions, dictionaries, tuples | Calculator, Word counter |
| 19-24 | Classes, objects, inheritance, error handling | Pet class, Bank account class |
| 25-30 | File I/O, JSON, randomness, timing, f-strings | To-do list app, Dice roller |

### Phase 2: Adventure Game Core (Lessons 31-45)

**Goal**: Build the RPG piece by piece

| Lessons | Classes/Features |
|---------|-----------------|
| 31-36 | Hero, Item, Weapon, Potion classes |
| 37-40 | Monster class, combat system, attack/flee |
| 41-43 | Shop, world map, game loop |
| 44-45 | Save/load system (JSON) |

### Phase 3: Polish & Mastery (Lessons 46-50)

**Goal**: Colors, UI, final integration, sharing

| Lessons | Features |
|---------|----------|
| 46-47 | Color system (ANSI), decorative UI |
| 48-49 | Objectives, final integration |
| 50 | Play and share the completed game |

## Lesson Format

Each lesson follows this structure:

1. **Story Hook**: A short narrative connecting to the game
2. **Concept Explanation**: Simple explanation with examples
3. **Guided Steps**: Fill-in-the-blank code with clear instructions
4. **Test It**: Run tests to verify correctness
5. **Challenge**: Optional harder problem for advanced students
6. **Badge**: Unlock a badge for completing the lesson

## Auto-Test System

Each lesson has a corresponding test file. The `run_lesson.py` script:

1. Displays lesson instructions
2. Opens the scaffold file for editing
3. Runs tests with friendly output (green checkmarks, helpful hints)
4. Tracks progress in `progress.json`
5. Shows a badge when complete

### Example Test

```python
# tests/test_31.py
def test_hero_has_name():
    hero = Hero("Alex")
    assert hero.name == "Alex", "Hero name should be 'Alex'"

def test_hero_starts_with_100_health():
    hero = Hero("Alex")
    assert hero.health == 100, "Hero should start with 100 HP"

def test_hero_starts_with_50_gold():
    hero = Hero("Alex")
    assert hero.gold == 50, "Hero should start with 50 gold"
```

### Example Lesson Scaffold

```python
# lessons/31_hero_class.py
"""
Lesson 31: Build the Hero Class
================================

Your hero needs stats! In this lesson, you'll create a Hero class
with health, gold, and a name.

Step 1: Create the Hero class
  Add a class called Hero below.
  It should have:
  - name (a string)
  - health (starts at 100)
  - gold (starts at 50)

Step 2: Test your code
  Run: python run_lesson.py 31
"""

# Your code here:
# class Hero:
#     def __init__(self, name):
#         self.name = ???
#         self.health = ???
#         self.gold = ???
```

## Progress Tracking

Progress is saved in `progress.json`:

```json
{
  "current_lesson": 1,
  "completed": [],
  "badges": [],
  "total_time_minutes": 0,
  "streak_days": 0
}
```

Badges are awarded for:
- **Variables Master**: Complete lessons 1-3
- **Loop Wizard**: Complete lessons 11-13
- **Function Pro**: Complete lessons 14-16
- **Class Creator**: Complete lessons 19-23
- **File Handler**: Complete lessons 25-27
- **Hero Builder**: Complete lessons 31-36
- **Combat Master**: Complete lessons 37-40
- **Shop Keeper**: Complete lessons 41-43
- **Game Designer**: Complete lessons 44-50
- **Adventure Complete**: Finish all 50 lessons

## Key Design Principles for an 11-Year-Old

1. **Micro-lessons**: 15-30 min each, completable in one sitting
2. **Immediate feedback**: Tests show green checkmarks or encouraging hints
3. **Visual rewards**: Badges, progress bars, emoji celebrations
4. **Story integration**: Each lesson adds to the adventure narrative
5. **Safe mistakes**: Tests catch errors with messages like "Almost! Check your self. references"
6. **Growing pride**: Each lesson adds visible features to the game
7. **Parent dashboard**: README includes a progress tracking table

## Implementation Plan

1. Create directory structure
2. Write `run_lesson.py` runner with test framework
3. Write lessons 1-10 with scaffolds and tests
4. Verify lessons 1-10 work end-to-end
5. Write lessons 11-30 with scaffolds and tests
6. Write lessons 31-50 with scaffolds and tests
7. Write README.md with student/parent instructions
8. Final verification of all 50 lessons

## Running the Curriculum

```bash
# Start with lesson 1
python run_lesson.py 1

# Run any lesson
python run_lesson.py <lesson_number>

# Run all tests
python run_lesson.py --all

# Show progress
python run_lesson.py --progress
```

## For Parents and Teachers

- Each lesson takes 15-30 minutes
- No prior Python knowledge required
- Lessons build on each other, but each is self-contained
- Tests provide immediate feedback
- Progress is saved automatically
- The final game can be played and shared with friends and family
