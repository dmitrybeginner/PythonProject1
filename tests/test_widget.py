import pytest
from src.widget import mask_account_card

@pytest.mark.parametrize("input_string, expected", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),  # Исправлено
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
])
def test_mask_account_card(input_string, expected):
    assert mask_account_card(input_string) == expected