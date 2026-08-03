"""Meta-tests for lesson instruction quality.

Naive students need complete, verbose, correctly-rendering instructions.
These tests enforce the contract in scaffolds/TEMPLATE.md so a lesson can
never silently regress to a 30-word command list.
"""
import ast
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCAFFOLDS_DIR = ROOT / "scaffolds"
TOTAL_LESSONS = 50
LESSON_NUMBERS = list(range(1, TOTAL_LESSONS + 1))

REQUIRED_SECTIONS = [
    "WHAT YOU'LL LEARN",
    "NEW WORDS",
    "HOW IT WORKS",
    "YOUR TASK",
    "EXAMPLE",
    "WHEN IT WORKS YOU'LL SEE",
    "IF YOU GET STUCK",
    "CHECK YOUR WORK",
]

# Minimum words of instruction. The old scaffolds averaged 32 words, which
# is far too thin to teach a concept to a beginner.
MIN_WORDS = 120


def _scaffold(num):
    matches = sorted(SCAFFOLDS_DIR.glob(f"{num:02d}_*.py"))
    assert matches, f"Lesson {num} has no scaffold"
    return matches[0]


def _instructions(num):
    """The rendered docstring exactly as the student will read it."""
    text = _scaffold(num).read_text()
    doc = ast.get_docstring(ast.parse(text))
    assert doc, f"Lesson {num} scaffold has no instruction docstring"
    return doc


def test_every_lesson_has_all_sections():
    problems = {}
    for n in LESSON_NUMBERS:
        doc = _instructions(n)
        missing = [s for s in REQUIRED_SECTIONS if s not in doc]
        if missing:
            problems[n] = missing
    assert not problems, f"Lessons missing template sections: {problems}"


def test_instructions_are_verbose_enough():
    thin = {
        n: len(_instructions(n).split())
        for n in LESSON_NUMBERS
        if len(_instructions(n).split()) < MIN_WORDS
    }
    assert not thin, (
        f"These lessons are too thin for a beginner (min {MIN_WORDS} words): {thin}"
    )


def test_step_numbers_are_sequential_with_no_gaps():
    """'Step 1, Step 2, Step 4' makes a child think they lost a page."""
    broken = {}
    for n in LESSON_NUMBERS:
        steps = [int(s) for s in re.findall(r"Step (\d+):", _instructions(n))]
        if steps != list(range(1, len(steps) + 1)):
            broken[n] = steps
    assert not broken, f"Lessons with broken step numbering: {broken}"


def test_every_lesson_defines_at_least_one_new_word():
    empty = []
    for n in LESSON_NUMBERS:
        doc = _instructions(n)
        section = doc.split("NEW WORDS", 1)[1].split("HOW IT WORKS", 1)[0]
        if len([ln for ln in section.splitlines() if ln.strip()]) < 2:
            empty.append(n)
    assert not empty, f"Lessons with an empty NEW WORDS section: {empty}"


def test_escape_sequences_render_literally():
    r"""A lesson teaching \n must show \n, not an actual newline.

    Such lessons must use a raw docstring (r\"\"\"...\"\"\").
    """
    broken = []
    for n in LESSON_NUMBERS:
        raw = _scaffold(n).read_text()
        doc = _instructions(n)
        # If the source mentions a tab/newline escape but the rendered
        # docstring has lost it, the docstring needed the r prefix.
        if "\\t" in raw and "\\t" not in doc:
            broken.append(n)
    assert not broken, (
        f"These lessons teach escape sequences but render them as real "
        f"whitespace; use a raw docstring: {broken}"
    )


def test_no_triple_quote_escapes_leak_into_instructions():
    r"""Escaped triple quotes (\"\"\") look like line noise to a beginner."""
    ugly = [n for n in LESSON_NUMBERS if '\\"' in _instructions(n)]
    assert not ugly, (
        f"These lessons show escaped quotes to the student: {ugly}. Use the "
        f"word 'docstring' or single quotes in the example instead."
    )


def test_check_your_work_names_the_right_lesson():
    wrong = []
    for n in LESSON_NUMBERS:
        if f"run_lesson.py {n}" not in _instructions(n):
            wrong.append(n)
    assert not wrong, (
        f"These lessons show the wrong 'python run_lesson.py N' command: {wrong}"
    )


def test_every_name_the_tests_require_is_named_in_the_instructions():
    """Rule 4: a student who follows the steps must be able to pass.

    If a test looks up a variable or function by name, the lesson has to
    tell the student to use that exact name.
    """
    tests_dir = ROOT / "tests"
    problems = {}
    for n in LESSON_NUMBERS:
        test_src = (tests_dir / f"test_{n:02d}.py").read_text()
        demanded = set(re.findall(r'run\.get\("(\w+)"\)', test_src))
        demanded |= set(re.findall(r'defines_(?:function|class)\(\d+, "(\w+)"\)', test_src))
        doc = _instructions(n).lower()
        missing = sorted(d for d in demanded if d.lower() not in doc)
        if missing:
            problems[n] = missing
    assert not problems, (
        f"Tests require names the lesson never mentions (unpassable by "
        f"following instructions): {problems}"
    )
