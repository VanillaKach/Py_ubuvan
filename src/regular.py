import re
from collections import Counter
from typing import Dict, List


def search_operations(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Функция ищет в списке словарей операций по заданной строке.
    """
    # Используем re.search с учетом границ слов и игнорированием регистра
    pattern = re.compile(r'\b{}\b'.format(re.escape(search_string)), flags=re.IGNORECASE)
    result = []
    for transaction in transactions:
        # Преобразуем description в строку, чтобы избежать TypeError
        description = str(transaction.get('description', ''))
        if pattern.search(description):
            result.append(transaction)
    return result


def count_operations_by_type(transactions: List[Dict], categories: Dict[str, str]) -> Dict[str, int]:
    """
    Функция подсчитывает количество банковских операций определенного типа.
    """
    # Используем Counter для подсчета операций по категориям
    counter: Counter[str] = Counter()
    for transaction in transactions:
        description = transaction.get('description', '')  # Получаем описание операции
        print(f"Описание операции: {description}")  # Отладочный вывод
        category = categories.get(description, 'Other')  # Определяем категорию
        print(f"Категория: {category}")  # Отладочный вывод
        counter[category] += 1
    return dict(counter)
