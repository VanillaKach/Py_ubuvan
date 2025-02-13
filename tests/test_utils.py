import unittest
from unittest.mock import mock_open, patch
from src.utils import load_transactions

class TestLoadTransactions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    @patch("os.path.isfile", return_value=True)  # Мокируем проверку существования файла
    def test_load_transactions_success(self, mock_isfile, mock_file):
        result = load_transactions("dummy_path.json")
        expected = [{"amount": 100, "currency": "USD"}]
        self.assertEqual(result, expected)

    @patch("builtins.open", new_callable=mock_open, read_data="not a json")
    @patch("os.path.isfile", return_value=True)  # Мокируем проверку существования файла
    def test_load_transactions_invalid_json(self, mock_isfile, mock_file):
        result = load_transactions("dummy_path.json")
        self.assertEqual(result, [])

    @patch("os.path.isfile", return_value=False)  # Мокируем, чтобы файл не существовал
    def test_load_transactions_file_not_found(self, mock_isfile):
        result = load_transactions("dummy_path.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    @patch("os.path.isfile", return_value=True)  # Мокируем проверку существования файла
    def test_load_transactions_not_a_list(self, mock_isfile, mock_file):
        result = load_transactions("dummy_path.json")
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()