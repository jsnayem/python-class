"""Tests for Lesson 27: JSON - Save Game Data."""
import json
import os
import tempfile

from _helpers import (
    assert_scaffold_is_blank,
    lesson_path,
    requires_student_code,
    run_student,
    safe_stdin,
)


def test_scaffold_has_no_answer():
    assert_scaffold_is_blank(27)


def test_save_data_dictionary_exists():
    run = run_student(27)
    assert isinstance(run.get("save_data"), dict), "Step 1: create save_data as a dict."


def test_writes_a_real_savegame_json():
    requires_student_code(27)
    tmp = tempfile.mkdtemp()
    cwd = os.getcwd()
    try:
        os.chdir(tmp)
        import io
        from contextlib import redirect_stdout

        with safe_stdin(), redirect_stdout(io.StringIO()):
            exec(compile(lesson_path(27).read_text(), "lesson27", "exec"), {})
        assert os.path.exists("savegame.json"), (
            "Step 2: write the data to a file called savegame.json."
        )
        data = json.load(open("savegame.json"))
    finally:
        os.chdir(cwd)
    assert isinstance(data, dict) and data, (
        "Step 2: savegame.json should contain your save_data dictionary."
    )


def test_prints_the_loaded_name():
    run = run_student(27)
    name = run.get("save_data", {}).get("name")
    assert name is not None, "Step 1: save_data should have a 'name' key."
    assert str(name) in run.output, "Step 3: read the file back and print the name."
