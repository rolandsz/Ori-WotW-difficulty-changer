from typing import Final

DEFAULT_DIFFICULTY_OFFSETS: Final[list[int]] = [0x145F, 0x1463, 0x279C]


def get_possible_difficulty_offsets(
    easy_bytes: bytes, medium_bytes: bytes, hard_bytes: bytes
) -> list[int]:
    """
    Heuristic solution for finding the difficulty offset(s) in the save files.

    The assumption is that the difficulty is stored as a single byte and
    the set of difficulties has consecutive numerical values.
    """
    data = zip(easy_bytes, medium_bytes, hard_bytes)

    return [
        i
        for i, (easy_byte, medium_byte, hard_byte) in enumerate(data)
        if hard_byte - medium_byte == medium_byte - easy_byte == 1
    ]
