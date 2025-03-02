from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def transactions_data() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state(transactions_data: List[Dict[str, Any]]) -> None:
    filtered_executed = filter_by_state(transactions_data)
    assert len(filtered_executed) == 2


def test_sort_by_date(transactions_data: List[Dict[str, Any]]) -> None:
    sorted_desc = sort_by_date(transactions_data, reverse=True)
    assert sorted_desc[0]["date"] == "2019-07-03T18:35:29.512364"
