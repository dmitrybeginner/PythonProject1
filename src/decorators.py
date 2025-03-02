from typing import Callable, Any, Optional


def filter_by_currency(transactions, currency_code):
    """
    Фильтрует транзакции по заданной валюте и возвращает итератор.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
    Возвращает итератор с описаниями транзакций.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[
            8:12
        ] + " " + f"{number:016d}"[12:16]


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Декоратор для логирования вызовов функций."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            log_message = f"{func.__name__} called\n"
            log_message += f"Inputs: args={args}, kwargs={kwargs}\n"

            try:
                result = func(*args, **kwargs)
                log_message += f"Result: {result}\n"
                log_message += f"{func.__name__} ok\n"
            except Exception as e:
                log_message += f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                raise
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)

            return result

        return wrapper

    return decorator
