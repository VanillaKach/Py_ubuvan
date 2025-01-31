from typing import List, Dict

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
# Вставить в строку 69 тест у декоратору*
# def test_multiply_success_to_file(cleanup_log_file: Any) -> None:
#     """Тест для успешного выполнения функции multiply с логированием в файл."""
#     result = multiply(3, 4)
#     assert result == 12
#
#     # Проверяем, что файл логов существует
#     assert os.path.exists("test_log.txt")
#
#     # Проверяем содержимое файла логов
#     with open("test_log.txt", "r") as log_file:
#         logs = log_file.read()
#         assert "multiply started with args: (3, 4), kwargs: {}" in logs
#         assert "multiply ok. Result: 12" in logs

