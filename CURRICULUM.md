# 50-Lesson Python Adventure Game Curriculum

## Overview

A scaffolded curriculum where a beginner (written for an 11-year-old with no
programming experience) builds a complete text-based RPG across 50 short
lessons. Every lesson introduces one concept, defines its vocabulary in plain
language, gives a worked example, and is graded by tests that run the
student's own code.

## How a lesson is written

Every scaffold follows the same eight-section shape, documented in
`scaffolds/TEMPLATE.md`:

| Section | Purpose |
|---|---|
| WHAT YOU'LL LEARN | The goal in one plain sentence |
| NEW WORDS | Every technical term defined at first use |
| HOW IT WORKS | The mechanism, with the code read aloud in English |
| YOUR TASK | Numbered steps; every test assertion traces to one |
| EXAMPLE | A worked example on a *different* topic, so nothing can be copied |
| WHEN IT WORKS YOU'LL SEE | The expected output, so 'done' is unambiguous |
| IF YOU GET STUCK | The real error messages the student will hit |
| CHECK YOUR WORK | The exact command to run |

`tests/test_meta_lesson_quality.py` enforces this shape automatically.

## Directory structure

```
python-class/
├── lessons/         # the student's working files (edit these)
├── scaffolds/       # pristine starter templates + TEMPLATE.md
├── answer_key/      # reference solutions (teacher-side)
├── tests/           # one test file per lesson, plus meta-tests
├── run_lesson.py    # the interactive lesson runner
├── sync_lessons.py  # refresh instructions without losing student code
├── main.py          # the finished adventure game
├── GLOSSARY.md      # every term, defined, with the lesson that teaches it
└── progress.json    # the student's progress (git-ignored)
```


## Phase 1 - Python Fundamentals

| # | File | Concept | New vocabulary |
|---|---|---|---|
| 1 | `01_hello_world.py` | Hello, World! - Your First Program | `program`, `print()`, `string`, `run` |
| 2 | `02_variables.py` | Variables - Storing Information | `variable`, `=`, `integer`, `f-string` |
| 3 | `03_printing.py` | Printing with Style | `escape sequence`, `\n`, `\t`, `border` |
| 4 | `04_math.py` | Math - Calculations | `operator`, `expression`, `evaluate` |
| 5 | `05_strings.py` | Strings - Working With Text | `method`, `.upper()`, `.lower()`, `concatenate` |
| 6 | `06_input.py` | Input - Talking To The Player | `input()`, `prompt`, `if`, `==`, `condition` |
| 7 | `07_lists.py` | Lists - Holding Many Things | `list`, `element`, `index`, `.append()`, `enumerate()` |
| 8 | `08_if_statements.py` | If Statements - Making Decisions | `boolean`, `comparison`, `and`, `or` |
| 9 | `09_loops.py` | Loops - Repeating Without Retyping | `loop`, `while`, `for`, `iterate`, `+= 1` |
| 10 | `10_functions.py` | Functions - Naming A Job | `function`, `def`, `parameter`, `argument`, `call` |
| 11 | `11_loops_intro.py` | Functions - Making a Spell | `define`, `parameter`, `argument`, `body` |
| 12 | `12_while_loops.py` | Default Arguments - Optional Information | `default`, `optional`, `required` |
| 13 | `13_for_loops.py` | For Loops - Doing Something To Every Item | `for`, `iterate`, `range(3)`, `loop variable` |
| 14 | `14_functions_intro.py` | Calling A Function Many Times | `call`, `reuse`, `DRY` |
| 15 | `15_function_args.py` | Dictionaries - Labelled Information | `dictionary`, `key`, `value`, `.keys()`, `.values()` |
| 16 | `16_return_values.py` | Return Values - Sending An Answer Back | `return`, `None` |
| 17 | `17_dictionaries.py` | Classes - Designing Your Own Kind Of Thing | `class`, `object`, `__init__`, `self`, `attribute` |
| 18 | `18_tuples.py` | Tuples - Fixed Groups Of Values | `tuple`, `immutable`, `index`, `unpacking` |
| 19 | `19_classes_intro.py` | Inheritance - Building On Another Class | `inheritance`, `child class`, `override` |
| 20 | `20_objects.py` | Objects Interacting - A Simple Attack | `method`, `state`, `mutate` |
| 21 | `21_attributes.py` | Class Attributes - Shared By Everyone | `instance attribute`, `class attribute`, `class_item` |
| 22 | `22_methods.py` | Inheritance - A Weapon Is An Item | `base class`, `subclass`, `is-a` |
| 23 | `23_inheritance.py` | super() - Letting The Parent Do Its Job | `super()`, `super().__init__(...)`, `price`, `bonus`, `amount` |
| 24 | `24_try_except.py` | Error Handling - Surviving Bad Input | `exception`, `ValueError`, `try`, `except`, `int()` |
| 25 | `25_file_writing.py` | File Writing - Saving Something Forever | `file`, `open()`, `mode "w"`, `.write()`, `with` |
| 26 | `26_file_reading.py` | File Reading - Loading It Back | `mode "r"`, `.read()`, `.readlines()`, `.strip()`, `FileNotFoundError` |
| 27 | `27_json.py` | JSON - Saving Whole Structures | `module`, `import`, `JSON`, `json.dump()`, `json.load()` |
| 28 | `28_random.py` | Random - Making The Game Unpredictable | `random`, `random.randint(1, 6)`, `simulate` |
| 29 | `29_time.py` | Time - Slowing Things Down | `time`, `suspense` |
| 30 | `30_f_strings.py` | F-Strings - Neat, Readable Output | `f-string`, `placeholder`, `format spec`, `:<10`, `:.1f` |

## Phase 2 - Building the Adventure Game

| # | File | Concept | New vocabulary |
|---|---|---|---|
| 31 | `31_hero_class.py` | The Hero Class - Your Adventure Begins | `class`, `__init__`, `self`, `attribute` |
| 32 | `32_hero_stats.py` | Hero Stats - Maximum Health And Staying Alive | `max_health`, `method`, `boolean`, `is_alive()` |
| 33 | `33_hero_inventory.py` | Hero Inventory - Carrying Things | `inventory`, `.append()`, `.remove()`, `per-object` |
| 34 | `34_item_class.py` | The Item Class - Things Worth Having | `base class`, `description`, `value` |
| 35 | `35_weapon_class.py` | Weapon And Potion - Two Kinds Of Item | `subclass`, `super()`, `heal_amount` |
| 36 | `36_potion_class.py` | The Potion Class - Healing Up | `heal_amount`, `min()`, `cap` |
| 37 | `37_monster_class.py` | The Monster Class - Something To Fight | `attack_power`, `gold_reward`, `max()` |
| 38 | `38_combat_system.py` | The Combat System - Landing A Blow | `attack(hero, monster)`, `equipped`, `None`, `unarmed` |
| 39 | `39_attack_logic.py` | The Damage Formula - Attack Minus Defense | `calculate_damage`, `attacker`, `defender`, `defense`, `floor` |
| 40 | `40_flee_mechanic.py` | The Flee Mechanic - Running Away | `flee`, `chance`, `random.random()`, `probability` |
| 41 | `41_shop_system.py` | The Shop - Spending Your Gold | `shop`, `item_key`, `in`, `afford` |
| 42 | `42_world_map.py` | The World Map - Places And Paths | `world`, `nested`, `exits`, `.get()` |
| 43 | `43_game_loop.py` | The Game Loop - Actually Travelling | `current`, `game loop`, `state`, `update` |
| 44 | `44_save_system.py` | The Save System - Remembering Progress | `save_game()`, `savegame.json`, `json.dump()`, `serialise` |
| 45 | `45_load_system.py` | The Load System - Continuing The Adventure | `load_game()`, `json.load()`, `FileNotFoundError`, `graceful` |
| 46 | `46_color_system.py` | Colors - Making The Terminal Glow | `ANSI escape code`, `Color`, `constant`, `RESET`, `colorize()` |
| 47 | `47_decorative_ui.py` | Decorative UI - A Banner Worth Looking At | `banner`, `border`, `separator`, `.center()` |
| 48 | `48_objectives.py` | Objectives - A Quest Checklist | `objectives`, `tuple`, `flag`, `unpacking` |
| 49 | `49_final_integration.py` | Final Integration - Putting It All Together | `integration`, `print_header()`, `load_game()`, `hero` |
| 50 | `50_play_and_share.py` | Play And Share - You Did It | `credits`, `call`, `ship` |

## Running the course

```bash
python run_lesson.py        # interactive menu
python run_lesson.py 7      # jump to one lesson
```

After editing lesson instructions, refresh the student's copies:

```bash
python sync_lessons.py           # dry run
python sync_lessons.py --apply   # write changes (backs up lessons/ first)
```

## Grading rules

Tests are behaviour-based, not text-matching:

- The lesson docstring is stripped before the student's code is examined, so
  no test can be satisfied by words in the instructions.
- A blank scaffold always fails, guarded by `tests/test_meta_suite_quality.py`.
- Every name a test requires is stated in the lesson, so following the steps
  is always enough to pass. This is checked automatically.

See `tests/README.md` for the full contributor rules.
