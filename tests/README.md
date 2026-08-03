# How the tests work (teacher / contributor notes)

The suite grades **behaviour**, not spelling. A student who follows the
lesson instructions passes; a student who writes correct code in a different
but valid style also passes.

## The four rules

Every lesson test module must obey these. `tests/test_meta_suite_quality.py`
enforces them automatically.

1. **Never assert against the instruction docstring.**
   Read the student's code with `student_code(n)` (docstring stripped) or run
   it with `run_student(n)`. Asserting `"class " in lesson_file.read_text()`
   is always a false pass: the instructions themselves contain the word.

2. **Assert behaviour, not source text.**
   `assert run.get("hero_gold") == 70` — not `assert "hero_gold + 20" in src`.
   The second form forbids the equally correct `hero_gold += 20`.
   When you must inspect structure (does a `for` loop exist? is a function
   defined?), use the AST helpers `defines_function`, `defines_class`,
   `uses_node`, `count_calls` — never a substring search.

3. **A blank starter file must never pass.**
   Go through `run_student(n)` or call `requires_student_code(n)`. Every
   module also asserts `assert_scaffold_is_blank(n)` so a shipped scaffold can
   never leak the answer.

4. **Every assertion must trace to a written instruction.**
   If a test requires a value, a name, or a behaviour, the lesson docstring
   must say so in a numbered step. Failure messages quote the step
   (`"Step 2: hero_gold should be 70..."`) so a stuck 11-year-old knows
   exactly where to look. If you want to test something new, add the step to
   the lesson first.

## Helpers (`tests/_helpers.py`)

| Helper | Use |
|---|---|
| `run_student(n)` | Execute the student's lesson; returns `.ns` (namespace) and `.output` (stdout). Guards for real code, stubs stdin, times out after 5s, runs in a temp dir so file lessons never touch the repo. |
| `student_code(n)` | Their code as text, instruction docstring removed. |
| `requires_student_code(n)` | Fail with a friendly message when nothing has been written. |
| `defines_function/defines_class/uses_node/count_calls` | AST checks that don't care about formatting. |
| `assert_scaffold_is_blank(n)` | The shipped starter must contain only instructions + the TODO line. |
| `load_answer(name)` | Teacher reference from `answer_key/`. Name such tests `test_reference_*` — the meta-guard exempts them, because they intentionally pass without student code. |

## The meta-guard

`test_no_lesson_passes_on_a_blank_starter` copies every scaffold over a
throwaway `lessons/` tree and runs all 50 test modules. If a lesson's whole
suite passes with no student code, that lesson is a **false completion** and
the test fails. This is the regression guard for the entire redesign — do not
delete it.

## Running

```
uv run --with pytest python -m pytest tests -q     # everything
python run_lesson.py 7                             # one lesson, student view
```

`run_lesson.py` executes the same test files with its own stdlib runner, so
tests must not import pytest-only features (no fixtures, no `parametrize`).
