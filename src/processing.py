def filter_by_state(transactions_list: list[dict[str, str | int]], state: str = 'EXECUTED') -> list[dict[str, str | int]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param transactions_list: Список словарей с транзакциями.
    :param state: Значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список словарей.
    """
    return [transaction for transaction in transactions_list if transaction.get('state') == state]


def sort_by_date(transactions_list: list[dict[str, str | int]], reverse: bool = True) -> list[dict[str, str | int]]:
    """
    Сортирует список словарей по ключу 'date'.

    :param transactions_list: Список словарей с транзакциями.
    :param reverse: Флаг сортировки по убыванию (по умолчанию True).
    :return: Отсортированный список словарей.
    """
    return sorted(transactions_list, key=lambda x: x['date'], reverse=reverse)


# Пример входных данных для проверки функций
transactions_data: list[dict[str, str | int]] = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Пример работы функции filter_by_state
filtered_executed: list[dict[str, str | int]] = filter_by_state(transactions_data)
print(filtered_executed)

# Пример работы функции sort_by_date
sorted_transactions: list[dict[str, str | int]] = sort_by_date(transactions_data)
print(sorted_transactions)
