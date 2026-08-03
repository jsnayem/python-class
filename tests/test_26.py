"""Tests for Lesson 26: File Reading."""
import os
import tempfile

from _helpers import (
    assert_scaffold_is_blank,
    count_calls,
    lesson_path,
    requires_student_code,
    safe_stdin,
)


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(26)


def test_opens_a_file_for_reading():
    requires_student_code(26)
    assert count_calls(26, "open") >= 1, "Step 1: use open() to read save.txt."


def _run_with_save_file(text):
    """Run the lesson in a temp dir that already contains save.txt."""
    import io
    from contextlib import redirect_stdout

    requires_student_code(26)
    tmp = tempfile.mkdtemp()
    cwd = os.getcwd()
    buf = io.StringIO()
    try:
        os.chdir(tmp)
        with open("save.txt", "w") as f:
            f.write(text)
        with safe_stdin(), redirect_stdout(buf):
            exec(compile(lesson_path(26).read_text(), "lesson26", "exec"), {})
    finally:
        os.chdir(cwd)
    return buf.getvalue()


def test_prints_the_name_and_score_it_read():
    output = _run_with_save_file("Zelda\n999\n")
    assert "Zelda" in output, "Step 2: print the name you read from the file."
    assert "999" in output, "Step 2: print the score you read from the file."


def test_reads_whatever_the_file_contains():
    # Proves the values come from the file, not from hard-coded text.
    output = _run_with_save_file("Mira\n17\n")
    assert "Mira" in output and "17" in output, (
        "Your code should print what save.txt actually contains, not a "
        "hard-coded name."
    )
