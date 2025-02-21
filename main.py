from typing import Any, Dict, List

from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card
from src.working_with_tables import read_transactions_from_csv, read_transactions_from_excel


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice: str = input("Пользователь: ")
    transactions: List[Dict[str, Any]]  # Инициализируем переменную без значения

    if choice == "1":
        transactions = load_transactions("data/operations.json")
    elif choice == "2":
        transactions = read_transactions_from_csv("data/transactions.csv")
    elif choice == "3":
        transactions = read_transactions_from_excel("data/transactions_excel.xlsx")
    else:
        print("Некорректный выбор.")
        return

    while True:
        state: str = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: "
        )
        if state.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print(f'Статус операции "{state}" недоступен.')

    filtered_transactions: List[Dict[str, Any]] = filter_by_state(transactions, state)
    print(f'Операции отфильтрованы по статусу "{state}".')

    sort_choice: str = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_choice == "да":
        order_choice: str = input("Отсортировать по возрастанию или по убыванию?  возрастанию/по убыванию\nПользователь: ").strip().lower()
        descending: bool = order_choice == "по убыванию"
        filtered_transactions = sort_by_date(filtered_transactions, descending)

    currency_filter: str = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if currency_filter == "да":
        filtered_transactions = [trans for trans in filtered_transactions if trans.get("currency_code") == "RUB"]

    description_filter: str = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ")
        .strip()
        .lower()
    )
    if description_filter == "да":
        keyword: str = input("Введите слово для фильтрации по описанию:\nПользователь: ")
        filtered_transactions = [
            trans for trans in filtered_transactions if keyword.lower() in trans.get("description", "").lower()
        ]

    print("Распечатываю итоговый список транзакций...")

    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")
        for trans in filtered_transactions:
            date_formatted: str = get_date(trans["date"])
            description: str = trans["description"]
            amount: float = trans["amount"]
            currency: str = trans["currency_code"]
            from_account: str = mask_account_card(trans["from"]) if trans.get("from") else "Счет **0000"
            to_account: str = mask_account_card(trans["to"]) if trans.get("to") else "Счет **0000"

            print(f"{date_formatted} {description}")
            print(f"{from_account} -> {to_account}")
            print(f"Сумма: {amount} {currency}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()


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
