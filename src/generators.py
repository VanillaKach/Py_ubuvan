from typing import Any, Dict, Generator, Iterable, Iterator


def filter_by_currency(
    transactions: Iterable[Dict[str, Any]], currency_code: str
) -> Generator[Dict[str, Any], None, None]:
    """Фильтрует список транзакций по указанной валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


# Пример использования функции
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 123456789,
        "state": "EXECUTED",
        "date": "2020-01-01T00:00:00.000000",
        "operationAmount": {"amount": "1000.00", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод в евро",
        "from": "Счет 11111111111111111111",
        "to": "Счет 22222222222222222222",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions: Iterable[Dict[str, Any]]) -> Iterator[str]:
    """Генератор описаний транзакций"""
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


# Пример использования генератора
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 123456789,
        "state": "EXECUTED",
        "date": "2020-01-01T00:00:00.000000",
        "operationAmount": {"amount": "1000.00", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 11111111111111111111",
        "to": "Счет 22222222222222222222",
    },
]


def transaction_next_descriptions(transactions: Iterable[Dict[str, Any]]) -> Iterator[str]:
    """Генератор описаний транзакций"""
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


# Пример использования генератора
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 123456789,
        "state": "EXECUTED",
        "date": "2020-01-01T00:00:00.000000",
        "operationAmount": {"amount": "1000.00", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 11111111111111111111",
        "to": "Счет 22222222222222222222",
    },
]

descriptions = transaction_next_descriptions(transactions)
for _ in range(3):
    print(next(descriptions))


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор номеров карт"""
    for number in range(start, end + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[
            8:12
        ] + " " + f"{number:016d}"[12:]


# Пример использования генератора
for card_number in card_number_generator(1, 5):
    print(card_number)
