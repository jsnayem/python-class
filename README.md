# Python Adventure Game Curriculum

## Welcome! 🎮

This curriculum teaches Python programming by building a complete text-based RPG game. Each lesson is 15-30 minutes and builds on the previous one.

## Quick Start

```bash
python run_lesson.py
```

That's it — no arguments. The runner opens an interactive menu:

```
n        - Continue / retry current lesson
a        - Run ALL lesson tests
s        - Show progress
p <num>  - Open a completed lesson
i <num>  - Preview any lesson
r        - Reset everything
q        - Quit
```

## How It Works

1. **Learn** - Each lesson teaches one Python concept
2. **Write** - Fill in the code in `lessons/XX_*.py`
3. **Test** - Tests run automatically and give you instant feedback
4. **Earn** - Get badges and track your progress

## Progress Tracking

Your progress is saved in `progress.json`. You can see:
- Which lessons you've completed
- How much time you've spent
- Badges you've earned

## Directory Structure

```
python-class/
├── lessons/           # Your completed lesson code
├── tests/             # Test files (don't edit)
├── scaffolds/         # Original lesson templates
├── run_lesson.py      # The lesson runner
├── progress.json      # Your progress
└── main.py            # The adventure game (lessons 31-50)
```

## Badges

Complete lessons to earn badges:

| Badge | Lessons | Emoji |
|-------|---------|-------|
| Variables Master | 1-3 | 📊 |
| Loop Wizard | 11-13 | 🔄 |
| Function Pro | 14-16 | 🔧 |
| Class Creator | 19-23 | 🏗️ |
| File Handler | 25-27 | 📁 |
| Hero Builder | 31-36 | ⚔️ |
| Combat Master | 37-40 | 🗡️ |
| Shop Keeper | 41-43 | 🏪 |
| Game Designer | 44-50 | 🎮 |
| Adventure Complete | 50 | 🏆 |

## Tips for Success

1. **Don't rush** - Take your time with each lesson
2. **Read the whole lesson** - The instructions define every new word, show a
   worked example, and tell you exactly what the output should look like
3. **Look words up** - `GLOSSARY.md` explains every technical term in the course
4. **Read the error** - Each lesson has an "IF YOU GET STUCK" section listing
   the errors you are most likely to see and what they mean
5. **Have fun** - You're building a real game!

## How each lesson is written

Every lesson has the same eight parts, so you always know where to look:

| Section | What it gives you |
|---------|-------------------|
| WHAT YOU'LL LEARN | The goal, in one sentence |
| NEW WORDS | Every new technical word, in plain language |
| HOW IT WORKS | How the code works, read aloud in English |
| YOUR TASK | Numbered steps to follow |
| EXAMPLE | A worked example on a different topic to learn from |
| WHEN IT WORKS YOU'LL SEE | Exactly what your output should look like |
| IF YOU GET STUCK | The errors you might hit, and what they mean |
| CHECK YOUR WORK | The command that tests your work |

## Parent Guide

**What this teaches.** 50 lessons take a complete beginner from `print()` to a
working object-oriented game with save files, error handling and a shop. Each
lesson introduces exactly one concept and defines its vocabulary. See
`CURRICULUM.md` for the full lesson-by-lesson map, and `GLOSSARY.md` for every
term the course teaches.

**Time.** Each lesson takes 15-30 minutes. No prior Python knowledge is needed,
by you or the student.

**Red tests are normal and expected.** Until your child writes the code, every
lesson reports failures saying *"Lesson N has no student code yet"*. That is the
system working correctly, not a broken program. A test only passes when their
code genuinely does the right thing — instructions cannot be copied to fake it.

**How to read a failure.** Each failure names the step it came from, e.g.
*"Step 2: is_alive() is True while health > 0."* Point your child at that step
in the lesson. They are never expected to read Python tracebacks.

**Checking progress.** Run `python run_lesson.py` and press `s` to see completed
lessons, time spent and badges earned. Progress lives in `progress.json`.

**Playing the result.** After lesson 50, run `python main.py` to play the
finished game.

**Industry habits taught.** Alongside syntax, the course teaches conventions
real programmers use: `snake_case` naming, `PascalCase` classes, docstrings,
returning values instead of printing, catching specific exceptions, `with open`
for files, `UPPER_CASE` constants, and Don't Repeat Yourself. The full list is
at the bottom of `GLOSSARY.md`.

## Troubleshooting

**"Tests are failing"** - Read the message: it names the step you need. Then
check the "IF YOU GET STUCK" section of that lesson.

**"It says I have no student code"** - Write your code *below* the
`# TODO: Write your code...` line in `lessons/`, then save the file.

**"I want to start over"** - From the menu, choose `r` (Reset everything) and confirm with `y`

**"I want to play the game"** - Run `python main.py` (after completing lessons 31-50)

## For teachers and contributors

- `scaffolds/TEMPLATE.md` - the required shape of every lesson
- `tests/README.md` - the rules tests must follow (behaviour, never text matching)
- `python sync_lessons.py --apply` - push improved instructions into `lessons/`
  without deleting student work (backs up first)