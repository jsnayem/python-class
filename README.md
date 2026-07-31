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
2. **Read the hints** - Tests give helpful feedback
3. **Ask questions** - If stuck, try the hint or ask a grown-up
4. **Have fun** - You're building a real game!

## Parent Guide

- Each lesson takes 15-30 minutes
- No prior Python knowledge needed
- Progress is saved automatically
- The final game can be played with `python main.py`
- Tests provide immediate feedback

## Troubleshooting

**"Tests are failing"** - Read the error message carefully and check your code

**"I want to start over"** - From the menu, choose `r` (Reset everything) and confirm with `y`

**"I want to play the game"** - Run `python main.py` (after completing lessons 31-50)