import pytest
from typer.testing import CliRunner

from main import app
from ori_wotw_difficulty_changer.difficulty import Difficulty
from ori_wotw_difficulty_changer.offsets import DEFAULT_DIFFICULTY_OFFSETS
from tests.conftest import get_save_file_path

runner = CliRunner()


def test_find_difficulty_offsets():
    result = runner.invoke(
        app,
        [
            "find-difficulty-offsets",
            "--easy-path",
            get_save_file_path(Difficulty.Easy),
            "--medium-path",
            get_save_file_path(Difficulty.Medium),
            "--hard-path",
            get_save_file_path(Difficulty.Hard),
        ],
    )
    assert result.exit_code == 0

    for offset in DEFAULT_DIFFICULTY_OFFSETS:
        assert f"{offset:04X}" in result.stdout

    assert "Couldn't determine difficulty offsets" not in result.stdout


@pytest.mark.parametrize(
    "difficulty",
    [
        Difficulty.Easy,
        Difficulty.Medium,
        Difficulty.Hard,
    ],
)
def test_get_difficulty(difficulty: Difficulty):
    result = runner.invoke(
        app,
        [
            "get-difficulty",
            "--path",
            get_save_file_path(difficulty),
        ],
    )
    assert result.exit_code == 0
    assert f"{difficulty.name}" in result.stdout
    assert "Couldn't determine difficulty offsets" not in result.stdout


@pytest.mark.parametrize(
    "difficulty",
    [
        Difficulty.Easy,
        Difficulty.Medium,
        Difficulty.Hard,
    ],
)
def test_set_difficulty(difficulty: Difficulty):
    result = runner.invoke(
        app,
        [
            "set-difficulty",
            "--path",
            get_save_file_path(difficulty),
            "--difficulty",
            difficulty.value,
        ],
        input="y\ny\n",
    )

    assert result.exit_code == 0
    assert "Creating backup" in result.stdout
    assert "Patching file" in result.stdout
    assert "Done" in result.stdout
