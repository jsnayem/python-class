"""Shared test helpers.

Loads a module (lesson student file or answer_key/ reference) from a path
without polluting sys.modules. Resolves the Pyright "ModuleSpec | None"
complaint by guaranteeing a non-None spec from a known-existing file.
"""
import importlib.util
from pathlib import Path
from typing import Any

ROOT = Path(__file__).parent.parent


def load_module(modname: str, rel_path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(modname, rel_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {rel_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_answer(modname: str) -> Any:
    return load_module(modname, ROOT / "answer_key" / f"{modname}.py")


def lesson_text(num: int) -> str:
    path = ROOT / "lessons" / next((ROOT / "lessons").glob(f"{num:02d}_*.py"))
    return path.read_text()
