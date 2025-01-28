from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transact_data() -> List[Dict[str, Any]]:
    return [
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


@pytest.mark.parametrize(
    "currency_code, expected_count",
    [
        ("USD", 2),
        ("EUR", 1),
        ("JPY", 0),  # Транзакции в данной валюте отсутствуют
    ],
)
def test_filter_by_currency(transact_data: List[Dict[str, Any]], currency_code: str, expected_count: int) -> None:
    filtered_transactions = list(filter_by_currency(transact_data, currency_code))
    assert len(filtered_transactions) == expected_count


def test_filter_by_currency_empty_list() -> None:
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(transact_data: List[Dict[str, Any]]) -> None:
    descriptions = list(transaction_descriptions(transact_data))
    expected_descriptions = ["Перевод организации", "Перевод со счета на счет", "Перевод в евро"]
    assert descriptions == expected_descriptions


def test_transaction_descriptions_empty_list() -> None:
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start, end, expected_numbers",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
    ],
)
def test_card_number_generator(start: int, end: int, expected_numbers: List[str]) -> None:
    generated_numbers = list(card_number_generator(start, end))
    assert generated_numbers == expected_numbers


def test_card_number_generator_edge_cases() -> None:
    assert list(card_number_generator(0, 0)) == ["0000 0000 0000 0000"]
    assert list(card_number_generator(9999999999999999, 10000000000000000)) == [
        "9999 9999 9999 9999",
        "1000 0000 0000 0000",
    ]
