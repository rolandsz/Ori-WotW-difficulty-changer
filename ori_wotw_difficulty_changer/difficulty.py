import enum

from ori_wotw_difficulty_changer.offsets import DEFAULT_DIFFICULTY_OFFSETS


@enum.unique
class Difficulty(enum.Enum):
    Easy = "easy"
    Medium = "medium"
    Hard = "hard"

    @property
    def game_value(self) -> int:
        match self.name:
            case Difficulty.Easy.name:
                return 0
            case Difficulty.Medium.name:
                return 1
            case Difficulty.Hard.name:
                return 2


def maybe_get_difficulty(
    save_bytes: bytes, offsets: list[int] | None = None
) -> Difficulty | None:
    if offsets is None:
        offsets = DEFAULT_DIFFICULTY_OFFSETS

    values = [save_bytes[offset] for offset in offsets]

    for difficulty in Difficulty:
        if all(x == difficulty.game_value for x in values):
            return difficulty

    return None


def change_difficulty(
    save_bytes: bytes, difficulty: Difficulty, offsets: list[int] | None = None
) -> bytes:
    if offsets is None:
        offsets = DEFAULT_DIFFICULTY_OFFSETS

    save_bytes_array = bytearray(save_bytes)

    for offset in offsets:
        save_bytes_array[offset] = difficulty.game_value

    return bytes(save_bytes_array)
