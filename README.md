# Ori and the Will of the Wisps difficulty changer

Bosses are too hard, but you don’t want to restart the game from the beginning? Look no further!

![alt text](https://rolandszabo.com/assets/images/posts/ori/ori-wotw-difficulty-changer/result.jpg)

## Environment setup
```commandline
poetry install
```

## Usage

### Get difficulty of a save file
```commandline
> poetry run py main.py get-difficulty --path "C:\Users\<user>\AppData\Local\Ori and the Will of The Wisps\saveFile0.uberstate"
Difficulty: Medium
```

### Set difficulty of a save file
```commandline
> poetry run py main.py set-difficulty --path "C:\Users\<user>\AppData\Local\Ori and the Will of The Wisps\saveFile0.uberstate" --difficulty easy
Is the current difficulty 'medium'? [y/N]: y
Is the desired difficulty 'easy'? [y/N]: y
Creating backup C:\Users\<user>\AppData\Local\Ori and the Will of The Wisps\saveFile0.uberstate.bak.1687803860
Patching file C:\Users\<user>\AppData\Local\Ori and the Will of The Wisps\saveFile0.uberstate
Done
```

## Save file name mapping
| In-game slot (order) | Save file name      |
|----------------------|---------------------|
| 1                    | saveFile0.uberstate |
| 2                    | saveFile1.uberstate |
| ...                  | ...                 |

## Development
### Re-calculate offsets
```commandline
> poetry run py main.py find-difficulty-offsets --easy-path "./tests/save_files/saveFile_easy.uberstate" --medium-path "./tests/save_files/saveFile_medium.uberstate" --hard-path "./tests/save_files/saveFile_hard.uberstate"
Found possible difficulty offset: 0x145F
Found possible difficulty offset: 0x1463
Found possible difficulty offset: 0x279C
```

### QA
```
poetry run black .
poetry run ruff .
poetry run pytest
```
