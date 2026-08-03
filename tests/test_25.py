"""Tests for Lesson 25: File Writing.

The lesson runs inside a throwaway directory, so save.txt is created there
and never pollutes the repository.
"""
from _helpers import assert_scaffold_is_blank, count_calls, run_student


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(25)


def test_player_variables_exist():
    run = run_student(25)
    assert isinstance(run.get("player_name"), str), "Step 1: create player_name."
    assert run.get("player_gold") is not None, "Step 1: create player_gold."


def test_opens_a_file_for_writing():
    assert count_calls(25, "open") >= 1, "Step 1: use open() to create save.txt."
    assert count_calls(25, "write") >= 1, "Step 1: use .write() to save the data."


def test_writes_the_values_to_save_txt():
    import os
    import tempfile

    from _helpers import lesson_path, safe_stdin

    run = run_student(25, isolate_files=False)  # values only
    tmp = tempfile.mkdtemp()
    cwd = os.getcwd()
    try:
        os.chdir(tmp)
        with safe_stdin():
            exec(compile(lesson_path(25).read_text(), "lesson25", "exec"), {})
        assert os.path.exists("save.txt"), "Step 1: the file must be named save.txt."
        content = open("save.txt").read()
    finally:
        os.chdir(cwd)
    assert str(run.get("player_name")) in content, "Step 1: write the player name."
    assert str(run.get("player_gold")) in content, "Step 1: write the player gold."
