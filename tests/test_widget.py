import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("input_string, expected", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
])
def test_mask_account_card(input_string: str, expected: str) -> None:
    assert mask_account_card(input_string) == expected


def test_get_date() -> None:
    # Тест с корректной датой
    assert get_date("2019-08-26T10:50:58.294041") == "26.08.2019"

    # Тест с другой датой
    assert get_date("2023-01-15T12:30:45.123456") == "15.01.2023"

    # Тест с минимально допустимой датой
    assert get_date("0001-01-01T00:00:00.000000") == "01.01.0001"
