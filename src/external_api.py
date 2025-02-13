import os
import requests
from dotenv import load_dotenv
from typing import Dict, Any

# Загружаем переменные окружения из файла .env
load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data"
API_KEY = os.getenv('EXCHANGE_API_KEY')  # Токен доступа из .env


def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    """Получает курс обмена между двумя валютами.

    Args:
        from_currency (str): Код валюты, из которой конвертируем.
        to_currency (str): Код валюты, в которую конвертируем.

    Returns:
        float: Курс обмена.
    """
    # Формируем URL запроса
    url = f"{API_URL}/convert?from={from_currency}&to={to_currency}&amount=1"

    headers = {
        "apikey": API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверяем на статус ошибки
        data = response.json()

        # Извлекаем курс обмена и приводим к float
        return float(data.get('result', 0.0))
    except requests.RequestException as e:
        print(f"Ошибка при обращении к API: {e}")
        return 0.0


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """Конвертирует сумму транзакции в рубли.

    Args:
        transaction (Dict[str, Any]): Словарь с данными о транзакции, включая сумму и валюту.

    Returns:
        float: Сумма в рублях.
    """
    # Извлекаем сумму и валюту из объекта operationAmount
    operation_amount = transaction.get('operationAmount', {})
    amount = float(operation_amount.get('amount', 0.0))  # Приводим к float
    currency = str(operation_amount.get('currency', {}).get('code', 'RUB'))  # Получаем код валюты

    if currency == 'RUB':
        return amount
    elif currency in ['USD', 'EUR']:
        # Получаем курс обмена на рубли
        rate = get_exchange_rate(currency, 'RUB')
        return amount * rate
    else:
        print(f"Неизвестная валюта: {currency}. Не могу выполнить конвертацию.")
        return 0.0