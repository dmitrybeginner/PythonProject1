import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_string, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
        ("Счет 1234567890123456", "Счет **3456"),
    ],
)
def test_mask_account_card(input_string: str, expected: str) -> None:
    """
    Тестирование функции mask_account_card с различными входными данными.
    """
    assert mask_account_card(input_string) == expected


@pytest.mark.parametrize(
    "input_string, expected",
    [
        ("2019-08-26T10:50:58.294041", "26.08.2019"),  # Корректная дата
        ("2023-01-15T12:30:45.123456", "15.01.2023"),  # Другая дата
        ("0001-01-01T00:00:00.000000", "01.01.0001"),  # Минимально допустимая дата
    ],
)
def test_get_date_valid(input_string: str, expected: str) -> None:
    """
    Тестирование функции get_date с корректными входными данными.
    """
    assert get_date(input_string) == expected


@pytest.mark.parametrize(
    "input_string, expected_exception",
    [
        ("2023-13-01T12:30:45.123456", ValueError),  # Неправильный месяц
        ("", ValueError),  # Пустая строка
        ("2023", IndexError),  # Слишком короткая строка
    ],
)
def test_get_date_invalid(input_string: str, expected_exception: type[Exception]) -> None:
    """
    Тестирование функции get_date с некорректными входными данными.
    """
    with pytest.raises(expected_exception):
        get_date(input_string)
