import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    (7000792289606361, "7000 79** **** 6361"),
    (1234567812345678, "1234 56** **** 5678"),
    (9876543210123456, "9876 54** **** 3456"),
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("account_number, expected", [
    (73654108430135874305, "**4305"),
    (1234567890123456, "**3456"),
    (9876543210987654, "**7654"),
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected