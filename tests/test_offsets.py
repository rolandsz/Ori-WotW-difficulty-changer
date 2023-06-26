from ori_wotw_difficulty_changer.offsets import (
    get_possible_difficulty_offsets,
    DEFAULT_DIFFICULTY_OFFSETS,
)


def test_get_possible_difficulty_offsets(
    save_file_easy: bytes, save_file_medium: bytes, save_file_hard: bytes
):
    assert (
        get_possible_difficulty_offsets(
            easy_bytes=save_file_easy,
            medium_bytes=save_file_medium,
            hard_bytes=save_file_hard,
        )
        == DEFAULT_DIFFICULTY_OFFSETS
    )
