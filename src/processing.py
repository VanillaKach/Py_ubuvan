from datetime import datetime

def filter_by_state(transactions, state = "EXECUTED"):
    """
    Фильтрует список словарей по значению ключа 'state'.
    :param transactions: Список словарей с транзакциями.
    :param state: Значение для фильтрации по ключу 'state' (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список словарей.
    """
    return [transact for transact in transactions if transact.get('state') == state]

transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

print(filter_by_state(transactions))  # Фильтр по умолчанию 'EXECUTED'
print(filter_by_state(transactions, "CANCELED"))  # Фильтр по 'CANCELED'


def sort_by_date(work_data, reverse = True):
    """
    Сортирует список словарей по дате.

    :param work_data: Список словарей, каждый из которых содержит ключ 'date'.
    :param reverse: Если True, сортировка по убыванию (новые даты в начале).
    :return: Отсортированный список словарей.
    """
    # Сортировка по ключу 'date', преобразованному в объект datetime
    return sorted(work_data, key = lambda x: datetime.fromisoformat(x["date"]), reverse = reverse)


# Пример использования:
work_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

sorted_data = sort_by_date(work_data)
print(sorted_data)
