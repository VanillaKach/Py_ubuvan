from typing import Any, Dict, Generator, Iterable, Iterator

from main import transactions

transact = transactions()


def filter_by_currency(
    transact: Iterable[Dict[str, Any]], currency_code: str
) -> Generator[Dict[str, Any], None, None]:
    """Фильтрует список транзакций по указанной валюте"""
    for transaction in transact:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


usd_transactions = filter_by_currency(transact, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transact: Iterable[Dict[str, Any]]) -> Iterator[str]:
    """Генератор описаний транзакций"""
    for transaction in transact:
        yield transaction.get("description", "Описание отсутствует")


def transaction_next_descriptions(transact: Iterable[Dict[str, Any]]) -> Iterator[str]:
    """Генератор описаний транзакций"""
    for transaction in transact:
        yield transaction.get("description", "Описание отсутствует")


descriptions = transaction_next_descriptions(transact)
for _ in range(3):
    print(next(descriptions))


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор номеров карт"""
    # Проверяем, что начальное значение не превышает 16 цифр
    if start >= 10**16:
        raise ValueError("Номер карты не может превышать 16 цифр.")

    # Ограничиваем end до 10**16
    end = min(end, 10**16)

    for i in range(start, end + 1):
        # Форматируем номер карты как строку с 16 цифрами
        formatted_number = f"{i:016d}"
        # Формируем номер карты в нужном формате
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:16]}"


# Пример вызова
for card in card_number_generator(1, 5):
    print(card)
