from pathlib import Path

import pytest

from ori_wotw_difficulty_changer.difficulty import Difficulty


def get_save_file_path(difficulty: Difficulty) -> Path:
    return (
        Path(__file__).parent / "save_files" / f"saveFile_{difficulty.value}.uberstate"
    )


@pytest.fixture
def save_file_easy() -> bytes:
    with get_save_file_path(Difficulty.Easy).open(mode="rb") as f:
        return f.read()


@pytest.fixture
def save_file_medium() -> bytes:
    with get_save_file_path(Difficulty.Medium).open(mode="rb") as f:
        return f.read()


@pytest.fixture
def save_file_hard() -> bytes:
    with get_save_file_path(Difficulty.Hard).open(mode="rb") as f:
        return f.read()
