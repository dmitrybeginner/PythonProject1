from src.decorators import log
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


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """
    Пример функции, которая складывает два числа.
    """
    return x + y


@log()
def my_function_with_error(x: int, y: int) -> float:
    """
    Пример функции, которая вызывает ошибку.
    """
    return x / y


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат DD.MM.YYYY.
    """
    if not date_string:
        raise ValueError("Пустая строка")

    # Проверяем, что строка имеет достаточную длину
    if len(date_string) < 10:
        raise IndexError("Строка слишком короткая")

    # Извлекаем год, месяц и день
    year = date_string[:4]
    month = date_string[5:7]
    day = date_string[8:10]

    # Проверяем, что месяц и день корректны
    if not (1 <= int(month) <= 12):
        raise ValueError("Некорректный месяц")
    if not (1 <= int(day) <= 31):
        raise ValueError("Некорректный день")

    return f"{day}.{month}.{year}"
