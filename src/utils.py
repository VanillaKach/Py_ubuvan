import json
import os
from typing import Any, Dict, List


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из JSON файла.

    Args:
        file_path (str): Путь к JSON файлу.

    Returns:
        List[Dict[str, Any]]: Список транзакций или пустой список, если файл пустой или не найден.
    """
    # Проверяем, существует ли файл
    if not os.path.isfile(file_path):
        return []

    # Открываем и читаем файл
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return []

    # Проверяем, является ли данные списком
    if isinstance(data, list):
        return data
    return []


def main() -> None:
    """Основная функция для загрузки и отображения транзакций."""
    # Создаем абсолютный путь к файлу
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/operations.json")
    transactions = load_transactions(file_path)
    print(transactions)


if __name__ == "__main__":
    main()
