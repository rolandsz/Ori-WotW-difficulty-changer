import pytest

from ori_wotw_difficulty_changer.difficulty import (
    maybe_get_difficulty,
    Difficulty,
    change_difficulty,
)


@pytest.mark.parametrize(
    "difficulty,expected_value",
    [
        (Difficulty.Easy, 0),
        (Difficulty.Medium, 1),
        (Difficulty.Hard, 2),
    ],
)
def test_game_value(difficulty: Difficulty, expected_value: int):
    assert difficulty.game_value == expected_value


def test_maybe_get_difficulty(
    save_file_easy: bytes, save_file_medium: bytes, save_file_hard: bytes
):
    assert maybe_get_difficulty(save_file_easy) == Difficulty.Easy
    assert maybe_get_difficulty(save_file_medium) == Difficulty.Medium
    assert maybe_get_difficulty(save_file_hard) == Difficulty.Hard


@pytest.mark.parametrize(
    "difficulty",
    [
        Difficulty.Easy,
        Difficulty.Medium,
        Difficulty.Hard,
    ],
)
def test_change_difficulty(
    save_file_easy: bytes,
    save_file_medium: bytes,
    save_file_hard: bytes,
    difficulty: Difficulty,
):
    assert (
        maybe_get_difficulty((change_difficulty(save_file_easy, difficulty)))
        == difficulty
    )
    assert (
        maybe_get_difficulty((change_difficulty(save_file_medium, difficulty)))
        == difficulty
    )
    assert (
        maybe_get_difficulty((change_difficulty(save_file_hard, difficulty)))
        == difficulty
    )
