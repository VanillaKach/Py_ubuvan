import re
from collections import Counter
from typing import Dict, List, Optional, Any


def search_operations(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Функция ищет в списке словарей операций по заданной строке.
    """
    # Используем re.search с учетом границ слов и игнорированием регистра
    pattern = re.compile(r'\b{}\b'.format(re.escape(search_string)), flags=re.IGNORECASE)
    result: List[Dict[str, Any]] = []  # Явная аннотация типа для результата
    for transaction in transactions:
        # Преобразуем description в строку, чтобы избежать TypeError
        description = str(transaction.get('description', ''))
        if pattern.search(description):
            result.append(transaction)
    return result


def count_operations_by_type(
        transactions: List[Dict[str, Any]],
        categories: Optional[List[str]] = None,
        executed_only: bool = False
) -> Dict[str, int]:
    operation_counter: Counter = Counter()  # Явная аннотация типа для счетчика
    if categories is None:
        categories = []

    for transaction in transactions:
        if executed_only and transaction.get('state', '') != 'EXECUTED':
            continue

        description = transaction.get('description', '')

        # Определяем категорию операции
        if description in categories:
            category = description
        else:
            category = 'Другие'  # Если описание не входит в список категорий

        operation_counter[category] += 1

    return dict(operation_counter)