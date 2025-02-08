def filter_by_state(transactions: list[dict], state: str='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей, каждый из которых содержит ключ 'state'.
    :param state: Значение ключа 'state', по которому производится фильтрация (по умолчанию 'EXECUTED').
    :return: Новый список словарей, где значение ключа 'state' соответствует указанному.
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]

# Пример использования
if __name__ == "__main__":
    transactions = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
    print(filter_by_state(transactions))