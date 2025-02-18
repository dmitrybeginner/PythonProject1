import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def transactions_data():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

def test_filter_by_state(transactions_data):
    filtered_executed = filter_by_state(transactions_data)
    assert len(filtered_executed) == 2
    assert all(transaction['state'] == 'EXECUTED' for transaction in filtered_executed)

    filtered_canceled = filter_by_state(transactions_data, 'CANCELED')
    assert len(filtered_canceled) == 2
    assert all(transaction['state'] == 'CANCELED' for transaction in filtered_canceled)

def test_sort_by_date(transactions_data):
    sorted_desc = sort_by_date(transactions_data, reverse=True)
    assert sorted_desc[0]['date'] == '2019-07-03T18:35:29.512364'
    assert sorted_desc[-1]['date'] == '2018-06-30T02:08:58.425572'

    sorted_asc = sort_by_date(transactions_data, reverse=False)
    assert sorted_asc[0]['date'] == '2018-06-30T02:08:58.425572'
    assert sorted_asc[-1]['date'] == '2019-07-03T18:35:29.512364'