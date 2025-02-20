import pytest
from src.regular import count_operations_by_type, search_operations
from collections import Counter
from typing import List, Dict

# Фикстуры для тестов

@pytest.fixture
def sample_transactions_for_count() -> List[Dict]:
    """Фикстура для списка транзакций для подсчета"""
    return [
        {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "description": "Перевод организации"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364", "description": "Перевод организации"},
        {"id": 587085106, "state": "EXECUTED", "date": "2018-03-23T10:45:06.972075", "description": "Открытие вклада"},
        {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "description": "Перевод со счета на счет"},
    ]

@pytest.fixture
def sample_categories() -> List[str]:
    """Фикстура для списка категорий"""
    return [
        "Перевод организации",
        "Открытие вклада",
        "Перевод со счета на счет",
    ]

# Тесты для функции count_operations_by_type()

def test_count_operations_by_type(sample_transactions_for_count, sample_categories):
    expected_result = Counter({
        "Перевод организации": 2,
        "Открытие вклада": 1,
        "Перевод со счета на счет": 1,
    })
    result = count_operations_by_type(sample_transactions_for_count, sample_categories)
    assert result == dict(expected_result)

# Тесты для функции search_operations()

@pytest.fixture
def sample_transactions() -> List[Dict]:
    """Фикстура для списка транзакций"""
    return [
        {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "description": "Перевод организации"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364", "description": "Перевод организации"},
        {"id": 939719570, "state": "EXECUTED", "date":  "2018-06-30T02:08:58.425572", "description": "Перевод организации"},
        {"id": 587085106, "state": "EXECUTED", "date": "2018-03-23T10:45:06.972075", "description": "Открытие вклада"},
        {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "description": "Перевод со счета на счет"},
    ]

@pytest.mark.parametrize(
    "search_string, expected_ids",
    [
        ("Перевод организации", [441945886, 41428829, 939719570]),  # Найдены три операции
        ("Открытие вклада", [587085106]),                           # Найдена одна операция
        ("Перевод со счета на счет", [142264268]),                  # Найдена одна операция
        ("Не существует", []),                                      # Ничего не найдено
    ]
)
def test_search_operations(sample_transactions, search_string, expected_ids):
    results = search_operations(sample_transactions, search_string)
    actual_ids = [result["id"] for result in results]
    assert actual_ids == expected_ids