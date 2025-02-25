from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """
    Функция маскирует номер карты или счета в зависимости от типа, используя существующие функции.
    """
    parts = input_string.split()  # Разделяем входную строку на слова
    account_type = " ".join(parts[:-1])  # Извлекаем тип аккаунта (все слова, кроме последнего)
    account_number = parts[-1]  # Последний элемент — номер карты или счета

    # Проверяем, является ли номер числом
    if not account_number.isdigit():
        raise ValueError("Номер карты или счета должен состоять из цифр.")

    # Определяем, нужно ли маскировать как карту или как счет
    if "Visa" in account_type or "Maestro" in account_type or "MasterCard" in account_type:
        return f"{account_type} {get_mask_card_number(int(account_number))}"
    else:
        return f"{account_type} {get_mask_account(int(account_number))}"


def get_date(date_string: str) -> str:
    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[0:4]}"
