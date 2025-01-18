from typing import Any, Dict, List, Optional


def filter_by_state(transactions: list, state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    :param transactions: Список словарей с транзакциями.
    :param state: Значение для фильтрации по ключу 'state' (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список словарей.
    """
    return [transact for transact in transactions if transact.get("state") == state]


transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

print(filter_by_state(transactions))  # Фильтр по умолчанию 'EXECUTED'
print(filter_by_state(transactions, "CANCELED"))  # Фильтр по 'CANCELED'


def sort_by_date(data: List[Dict[str, Any]], descending: Optional[bool] = True) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по дате.

    :param data: Список словарей, содержащих поле 'date'.
    :param descending: Параметр, задающий порядок сортировки (по умолчанию True - убывание).
    :return: Новый список, отсортированный по дате.
    """
    return sorted(data, key=lambda x: x["date"], reverse=bool(descending))


# Пример входных данных для проверки функции
input_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Тестирование функции
sorted_data = sort_by_date(input_data)
print(sorted_data)
