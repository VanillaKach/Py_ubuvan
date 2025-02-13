import json
import logging
import os
from typing import Any, Dict, List

# Настройка логирования для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler("utils.log")
file_handler.setLevel(logging.DEBUG)

# Настройка форматирования логов
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из JSON файла.

    Args:
        file_path (str): Путь к JSON файлу.

    Returns:
        List[Dict[str, Any]]: Список транзакций или пустой список, если файл пустой или не найден.
    """
    logger.debug(f"Попытка загрузки транзакций из файла: {file_path}")

    # Проверяем, существует ли файл
    if not os.path.isfile(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    # Открываем и читаем файл
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.debug("Транзакции успешно загружены.")
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования JSON.")
        return []

    # Проверяем, является ли данные списком
    if isinstance(data, list):
        return data

    logger.error("Загруженные данные не являются списком.")
    return []


def main() -> None:
    """Основная функция для загрузки и отображения транзакций."""
    # Создаем абсолютный путь к файлу
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/operations.json")
    transactions = load_transactions(file_path)
    print(transactions)


if __name__ == "__main__":
    main()
