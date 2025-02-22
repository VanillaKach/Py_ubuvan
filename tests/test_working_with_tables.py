from typing import Any, Dict
from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.working_with_tables import read_transactions_from_csv, read_transactions_from_excel


# Тест для функции считывания из CSV
def test_read_transactions_from_csv() -> None:
    mock_data: str = (
        "id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n"
        "3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту"
    )

    with patch("builtins.open", mock_open(read_data=mock_data)):
        transactions = read_transactions_from_csv("fake_path.csv")
        assert len(transactions) == 2
        assert transactions[0]["id"] == "650703"
        assert transactions[1]["state"] == "EXECUTED"


# Тест для функции считывания из Excel
def test_read_transactions_from_excel() -> None:
    mock_data: Dict[str, Any] = {
        "id": [650703, 3598919],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        "amount": [16210, 29740],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"],
    }

    df = pd.DataFrame(mock_data)

    with patch("pandas.read_excel", return_value=df):
        transactions = read_transactions_from_excel("fake_path.xlsx")
        assert len(transactions) == 2
        assert transactions[0]["currency_name"] == "Sol"
        assert transactions[1]["amount"] == 29740


if __name__ == "__main__":
    pytest.main()
