def get_mask_card_number(card_number: int) -> str:
    """
    Функцию маскировки номера банковской карты
    :param card_number:
    :return:
    """
    card_number_str = str(card_number)
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Функцию маскировки номера банковского счета
    :param account_number:
    :return:
    """
    account_number_str = str(account_number)
    masked_number = f"**{account_number_str[-4:]}"
    return masked_number
