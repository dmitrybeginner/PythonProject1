def filter_by_state(transactions_list, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return [transaction for transaction in transactions_list if transaction["state"] == state]


def sort_by_date(transactions_list, reverse=True):
    """
    Сортирует список словарей по ключу 'date'.

    """
    return sorted(transactions_list, key=lambda x: x['date'], reverse=reverse)


