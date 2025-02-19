import sys
from typing import Dict, List

from src.regular import count_operations_by_type, search_operations
from src.working_with_tables import read_transactions_from_csv, read_transactions_from_excel


def transactions() -> List[Dict]:
    transact = [
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
    return transact


def main() -> None:
    """
    Функция main отвечает за основную логику проекта с пользователем и связывает
    функциональности между собой.
    """
    # Загрузим данные из CSV и Excel файлов
    csv_data: List[Dict] = read_transactions_from_csv("transactions.csv")
    excel_data: List[Dict] = read_transactions_from_excel("transactions_excel.xlsx")

    # Объединяем данные
    all_data: List[Dict] = csv_data + excel_data

    # Основной цикл взаимодействия с пользователем
    while True:
        print("\nМеню:")
        print("1. Поиск операций по описанию")
        print("2. Подсчет операций по категориям")
        print("3. Выход")

        choice: str = input("Выберите действие: ")

        if choice == "1":
            search_term: str = input("Введите строку для поиска: ")
            results: List[Dict] = search_operations(all_data, search_term)
            print(f"Найдено {len(results)} операций.")
            for operation in results:
                print(operation)

        elif choice == "2":
            categories: Dict[str, str] = {
                "Перевод организации": "Организационные переводы",
                "Открытие вклада": "Вклады",
                "Перевод со счета на счет": "Межсчетовые переводы",
            }
            result: Dict[str, int] = count_operations_by_type(all_data, categories)
            print("Количество операций по категориям:")
            for category, count in result.items():
                print(f"{category}: {count}")

        elif choice == "3":
            print("Завершение программы...")
            sys.exit(0)

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
