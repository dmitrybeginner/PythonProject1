import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize("input_string, expected", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
])
def test_mask_account_card(input_string: str, expected: str) -> None:
    assert mask_account_card(input_string) == expected
