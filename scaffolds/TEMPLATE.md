# Lesson authoring template

Every scaffold in `scaffolds/` uses this exact shape. The audience is a naive
11-year-old who has never programmed. Assume they know nothing and have not
read any other lesson today.

## Why it is shaped this way

| Section | Purpose | Rule |
|---|---|---|
| `WHAT YOU'LL LEARN` | One plain sentence of the goal | No jargon at all |
| `NEW WORDS` | Define every technical term **at first use** | Kid-language definition, then the term is used correctly forever after |
| `HOW IT WORKS` | Explain the mechanism, not just the syntax | Show the shape of the code and read it aloud in English |
| `YOUR TASK` | Numbered steps | **Every test assertion must trace to a step here** |
| `EXAMPLE` | A worked example on a **different topic** | Gives a pattern to imitate, never the answer to copy |
| `WHEN IT WORKS YOU'LL SEE` | Expected output | Naive students can't tell "done" from "nearly done" |
| `IF YOU GET STUCK` | The real error text they will hit | `IndentationError` means nothing until it's named in advance |
| `STYLE` | One industry habit, cumulative | Optional; only where a habit is naturally introduced |
| `CHECK YOUR WORK` | The exact command | Always last |

## Hard rules

1. **Steps are numbered 1, 2, 3… with no gaps.** A missing step number makes
   a child think they lost a page.
2. **Every name a test requires must be written in a step.** If the test does
   `run.get("calculate_damage")`, the lesson must literally say
   `calculate_damage`.
3. **The example must not be the answer.** If the task is about an inventory,
   the example uses spells. They must still write their own code.
4. **No `"""` inside the body.** The docstring is stripped by finding the
   first closing `"""`; an inner one truncates the instructions.
5. **Define a term before using it.** Check `GLOSSARY.md` — if the term is
   new to the course, it goes in `NEW WORDS` here.

## Style habits, by lesson

These are introduced one at a time and reinforced afterwards. Collected for
the student in `GLOSSARY.md`.

| Lesson | Habit |
|---|---|
| 2 | `snake_case` names that say what they hold |
| 3 | Comments explain *why*, not *what* |
| 10 | Docstrings on every function; functions do one job |
| 16 | `return` a value instead of printing inside a function |
| 17 | Constants in `UPPER_CASE` at the top of the file |
| 19 | `PascalCase` for classes vs `snake_case` for functions |
| 24 | Catch a specific exception, never a bare `except` |
| 25 | `with open(...) as f:` instead of manual `.close()` |
| 44 | Don't repeat yourself — reuse the function you already wrote |
