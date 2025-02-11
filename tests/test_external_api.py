import unittest
from unittest.mock import patch
from src.external_api import get_exchange_rate, convert_to_rub
from typing import Any  # Добавьте этот импорт

class TestCurrencyConversion(unittest.TestCase):

    @patch('src.external_api.get_exchange_rate')
    def test_convert_usd_to_rub(self, mock_get_exchange_rate: Any) -> None:
        mock_get_exchange_rate.return_value = 75.0
        transaction = {'amount': 100, 'currency': 'USD'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 7500.0)

    @patch('src.external_api.get_exchange_rate')
    def test_convert_eur_to_rub(self, mock_get_exchange_rate: Any) -> None:
        mock_get_exchange_rate.return_value = 85.0
        transaction = {'amount': 100, 'currency': 'EUR'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 8500.0)

    def test_convert_rub(self) -> None:
        transaction = {'amount': 100, 'currency': 'RUB'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 100.0)

    def test_convert_unknown_currency(self) -> None:
        transaction = {'amount': 100, 'currency': 'XYZ'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()