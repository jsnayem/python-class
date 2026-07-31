# python-class Improvement Plan

Goal: make `--all` trustworthy, improve curriculum hygiene, and set up source-of-truth
version control without touching non-project assets.

---

## Execution order

Recommended: P1 → P0 → P2/P3. P1 is safest and gives us a clean rollback point.

---

## P1 — Git repo + data hygiene

Files changed:  
- new `.gitignore`  
- new `.gitignore` commit only

Commands to run:
```bash
cd /home/nayem/Projects/python-class
git init
git checkout -b main
cat > .gitignore <<'EOF'
#-local state
progress.json
savegame.json
save.txt

# Python
__pycache__/
*.pyc
.venv/
.venv*/
.DS_Store

# IDE
.idea/
.vscode/
EOF
git add .gitignore
git commit -m "chore: add .gitignore for local state and python artifacts"
```

Verify:
- `git status` shows clean tree
- `python3 run_lesson.py --progress` still works

---

## P0 — Fix failing tests for completed lessons

Targeted tests: lessons that currently pass student work but fail under `--all`:
3, 4, 6, 7, 8, 9, 25, 27.

Constraints:
- do not change lesson files unless absolutely necessary
- make tests verify behavior or runtime output, not exact strings from one student
- keep scaffolds as-blank / no-solution as documented by `--reset`

### Commit 1: test_03.py — test title text generically
### Commit 2: test_04.py — test printed numeric result, not exact expression text
### Commit 3: test_06.py — test input prompt used and response variable stored, without hanging on stdin
### Commit 4: test_07.py — test list variable exists through namespace inspection instead of stdout sniff
### Commit 5: test_08.py — test both `if` branches fire, not fixed human-readable strings
### Commit 6: tests/test_25.py and tests/test_27.py — test creates/reads `save.txt` with temp path or swallows IOError

Verify after each commit:
```bash
python3 run_lesson.py --all
python3 run_lesson.py 3
python3 run_lesson.py 6
python3 run_lesson.py 25
python3 run_lesson.py 27
```

Success criteria: `--all` exit code 0 and no `❌ Some tests failed.`

---

## P0 fix — remove hidden input() hazard in test_49

`test_49.py` runs `exec(compile(...))` on a file that has top-level `input()`.
Two acceptable paths:
- A: bypass std interact in test via `monkeypatch` or redirected stdin
- B: change lesson 49 scaffold so `input()` only happens inside `if __name__ == "__main__":`

Recommended: path B, because it matches the runner’s own stated policy
(`# Don't execute lesson code (it may have input() calls)`).

```
commit: test(lesson 49): guard lesson startup input in __main__ block
```

Verify:
```bash
python3 run_lesson.py --all
```

---

## P2 — Scaffold / curriculum alignment

Audit scaffolds for blank-starter contract. Fix obvious full-solution scaffolds:

Target files: `scaffolds/01_hello_world.py`, `scaffolds/02_variables.py`,
`scaffolds/07_lists.py`, `scaffolds/10_functions.py`.

Each diff becomes its own file-scoped commit, one test added asserting the
scaffold does NOT contain the expected answer key string.

```
commit: chore(scaffolds): restore blank starter for lesson 01
commit: chore(scaffolds): restore blank starter for lesson 02
...
```

Verify:
```bash
python3 run_lesson.py --reset
git diff --stat
```

---

## P2 — Test isolation

Move tests that touch `savegame.json` / `save.txt` to use `Path(__file__).with_name("tmp")`
or pytest `tmp_path`. Add a small `tests/conftest.py` that creates `tests/tmp/` at session start.
Each file stays file-scoped.

```
commit: chore(tests): isolate file IO to tests/tmp with conftest.py
```

---

## P3 — `reset_progress()` confirmation gate

Add optional `--yes` flag; when both `--reset` and no `--yes`, prompt once.

```
commit: feat(runner): confirm before destructive reset
```

---

## P3 — DRY progress rendering in `run_lesson.py`

Extract `def render_progress_summary(progress, label="...") -> str:` and replace
the three copy-pasted progress blocks.

```
commit: refactor(runner): dedupe progress summary rendering
```

---

## Verification gate (last step)

```bash
cd /home/nayem/Projects/python-class
python3 run_lesson.py --all
python3 run_lesson.py --progress
python3 run_lesson.py --reset --yes
python3 - <<'PY'
import io, sys, contextlib
from pathlib import Path
for f in sorted(Path("scaffolds").glob("*.py")):
    t = f.read_text()
    print(f"{f.name}: lines={len(t.splitlines())}")
PY
python3 main.py < <(printf "n\nAlex\ny\n")
```

All steps use only stdlib; no network.