import csv
from typing import Any, Dict, List
import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    transactions: List[Dict[str, Any]] = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            transactions.append(row)  # row имеет тип Dict[str, str]
    return transactions


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    df = pd.read_excel(file_path)
    # Преобразуем ключи в строки
    transactions: List[Dict[str, Any]] = [
        {str(key): value for key, value in record.items()} for record in df.to_dict(orient="records")
    ]
    return transactions
