import csv
from typing import Any, Dict, List, Hashable

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    transactions: List[Dict[str, Any]] = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            transactions.append(row)
    return transactions


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    df = pd.read_excel(file_path)
    transactions: List[Dict[str, Any]] = df.to_dict(orient="records")
    return transactions
