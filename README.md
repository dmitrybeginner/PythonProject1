# Виджет
## Описание:
Виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/dmitrybeginner/PythonProject1.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Тестирование
1. Для запуска тестов используйте команду:
```
pytest
```
## Модуль `generators`

#### Фильтрация транзакций по валюте
```python
from src.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))