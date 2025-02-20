import os
from typing import Dict, List, Optional

from src.regular import search_operations
from src.utils import load_transactions
from src.working_with_tables import read_transactions_from_csv, read_transactions_from_excel


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice: str = input("Пользователь: ")

    transactions: List[Dict] = []

    if choice == "1":
        file_path = os.path.join(os.path.dirname(__file__), "../data/operations.json")
        transactions = load_transactions(file_path)
    elif choice == "2":
        file_path = os.path.join(os.path.dirname(__file__), "../transactions.csv")
        transactions = read_transactions_from_csv(file_path)
    elif choice == "3":
        file_path = os.path.join(os.path.dirname(__file__), "../transactions_excel.xlsx")
        transactions = read_transactions_from_excel(file_path)
    else:
        print("Неверный выбор. Завершение программы.")
        return

    # Запрос статуса
    status: Optional[str] = None
    valid_statuses: set[str] = {"executed", "canceled", "pending"}

    while status not in valid_statuses:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию. "
                       "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").lower()
        if status not in valid_statuses:
            print(f"Статус операции \"{status.upper()}\" недоступен.")

    print(f"Операции отфильтрованы по статусу \"{status.upper()}\"")

    # Фильтрация по статусу
    filtered_transactions: List[Dict] = [t for t in transactions if t.get('state', '').lower() == status]

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    # Запрос дополнительных фильтров
    sort_by_date: bool = input("Отсортировать операции по дате? Да/Нет\n").strip().lower() == "да"
    if sort_by_date:
        order: str = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
        if order == "по возрастанию":
            filtered_transactions.sort(key=lambda x: x.get('date') or '')
        elif order == "по убыванию":
            filtered_transactions.sort(key=lambda x: x.get('date') or '', reverse=True)

    only_rub: bool = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower() == "да"

    keyword_filter: bool = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower() == "да"
    if keyword_filter:
        search_string: str = input("Введите слово для фильтрации по описанию:\n")
        filtered_transactions = search_operations(filtered_transactions, search_string)

    # Вывод результатов
    if filtered_transactions:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            if only_rub and transaction.get('currency') != 'RUB':
                continue
            print(f"{transaction.get('date')} {transaction.get('description')}\n"
                  f"Счет {transaction.get('account')}\n"
                  f"Сумма: {transaction.get('amount')} {transaction.get('currency')}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()