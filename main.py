import logging
import shutil
import time
from pathlib import Path
from typing import Annotated

import typer

from ori_wotw_difficulty_changer.difficulty import (
    maybe_get_difficulty,
    Difficulty,
    change_difficulty,
)
from ori_wotw_difficulty_changer.offsets import get_possible_difficulty_offsets

app = typer.Typer()

_logger = logging.getLogger(__name__)


_save_file_path_options = typer.Option(
    exists=True,
    file_okay=True,
    dir_okay=False,
    writable=False,
    readable=True,
    resolve_path=True,
)


@app.command()
def get_difficulty(
    path: Annotated[
        Path,
        _save_file_path_options,
    ]
):
    with path.open(mode="rb") as save_f:
        if difficulty := maybe_get_difficulty(save_bytes=save_f.read()):
            typer.echo(f"Difficulty: {difficulty.name}")
        else:
            typer.secho("Couldn't determine difficulty", fg=typer.colors.RED)


@app.command()
def set_difficulty(
    path: Annotated[
        Path,
        _save_file_path_options,
    ],
    difficulty: Annotated[Difficulty, typer.Option(case_sensitive=False)],
):
    with path.open(mode="rb") as save_f:
        save_bytes = save_f.read()

    if current_difficulty := maybe_get_difficulty(save_bytes=save_bytes):
        if not typer.confirm(
            f"Is the current difficulty {current_difficulty.value!r}?"
        ):
            raise typer.Abort()

    if not typer.confirm(f"Is the desired difficulty {difficulty.value!r}?"):
        raise typer.Abort()

    backup_path = path.with_suffix(f".uberstate.bak.{int(time.time())}")

    typer.echo(f"Creating backup {backup_path}")
    shutil.copy(path, backup_path)

    if not backup_path.exists():
        typer.secho("Couldn't create backup", fg=typer.colors.RED)
        raise typer.Abort()

    typer.echo(f"Patching file {path}")
    with path.open(mode="wb") as save_f:
        save_f.write(change_difficulty(save_bytes=save_bytes, difficulty=difficulty))

    typer.echo("Done")


@app.command()
def find_difficulty_offsets(
    easy_path: Annotated[Path, _save_file_path_options],
    medium_path: Annotated[Path, _save_file_path_options],
    hard_path: Annotated[Path, _save_file_path_options],
):
    with easy_path.open(mode="rb") as easy_f, medium_path.open(
        mode="rb"
    ) as medium_f, hard_path.open(mode="rb") as hard_f:
        if not (
            indices := get_possible_difficulty_offsets(
                easy_bytes=easy_f.read(),
                medium_bytes=medium_f.read(),
                hard_bytes=hard_f.read(),
            )
        ):
            typer.secho("Couldn't determine difficulty offsets", fg=typer.colors.RED)

        for i in indices:
            typer.echo(f"Found possible difficulty offset: 0x{i:04X}")


if __name__ == "__main__":
    app()
