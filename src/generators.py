from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Generator[dict, Any, None]:
    """
    Фильтрует транзакции по заданной валюте и возвращает итератор.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[Any, Any, None]:
    """
    Возвращает итератор с описаниями транзакций.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, Any, None]:
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        yield (
            f"{number:016d}"[:4] + " " +
            f"{number:016d}"[4:8] + " " +
            f"{number:016d}"[8:12] + " " +
            f"{number:016d}"[12:16]
        )
