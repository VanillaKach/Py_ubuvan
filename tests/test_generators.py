import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тестирование функции filter_by_currency
def test_filter_by_currency() -> None:
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}},
    ]

    # Проверка фильтрации по валюте USD
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 1
    assert usd_transactions[0]["operationAmount"]["currency"]["code"] == "USD"

    # Проверка фильтрации по валюте, которая отсутствует
    eur_transactions = list(filter_by_currency(transactions, "JPY"))
    assert len(eur_transactions) == 0

    # Проверка на пустой список
    empty_transactions = list(filter_by_currency([], "USD"))
    assert len(empty_transactions) == 0


# Тестирование функции transaction_descriptions
def test_transaction_next_descriptions() -> None:
    transactions = [
        {"description": "Тестовая транзакция 1"},
        {"description": "Тестовая транзакция 2"},
        {"description": "Тестовая транзакция 3"},
    ]

    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == ["Тестовая транзакция 1", "Тестовая транзакция 2", "Тестовая транзакция 3"]

    # Проверка на пустой список
    empty_descriptions = list(transaction_descriptions([]))
    assert empty_descriptions == []


# Тестирование генератора card_number_generator
def test_card_number_generator() -> None:
    # Тестируем генерацию карт в диапазоне от 1 до 5
    generated_cards = list(card_number_generator(1, 5))
    expected_cards = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert generated_cards == expected_cards

    # Проверяем крайние значения
    edge_cards = list(card_number_generator(9999, 10001))
    expected_edge_cards = ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]
    assert edge_cards == expected_edge_cards

    # Проверка на диапазон, где начальное значение больше конечного
    invalid_range = list(card_number_generator(5, 1))
    assert invalid_range == []


# Для запуска тестов
if __name__ == "__main__":
    pytest.main()
