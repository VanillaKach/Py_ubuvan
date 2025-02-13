import unittest
from typing import Any
from unittest.mock import mock_open, patch

from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    def test_load_transactions_success(self, mock_file: Any) -> None:
        result = load_transactions("dummy_path.json")
        expected = [{"amount": 100, "currency": "USD"}]
        self.assertEqual(result, expected)

    @patch("builtins.open", new_callable=mock_open, read_data="not a json")
    def test_load_transactions_invalid_json(self, mock_file: Any) -> None:
        result = load_transactions("dummy_path.json")
        self.assertEqual(result, [])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_transactions_file_not_found(self, mock_file: Any) -> None:
        result = load_transactions("dummy_path.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_load_transactions_not_a_list(self, mock_file: Any) -> None:
        result = load_transactions("dummy_path.json")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
