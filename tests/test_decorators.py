import logging
import os
from typing import Any, Generator

import pytest

from src.decorators import log  # Импортируем декоратор из модуля, где он определён


# Простая функция для тестирования
@log()
def add(x: int, y: int) -> int:
    return x + y


@log()
def divide(x: int, y: int) -> float:
    if y == 0:
        raise ValueError("Division by zero")
    return x / y


@log(filename="test_log.txt")
def multiply(x: int, y: int) -> int:
    return x * y


@pytest.fixture
def cleanup_log_file() -> Generator[None, None, None]:
    """Фикстура для очистки файла логов перед и после тестов."""
    log_file = "test_log.txt"
    if os.path.exists(log_file):
        os.remove(log_file)
    yield  # Выполняем тест
    if os.path.exists(log_file):
        os.remove(log_file)


def test_add_success(caplog: Any) -> None:
    """Тест для успешного выполнения функции add с выводом в консоль."""
    with caplog.at_level(logging.INFO):  # Устанавливаем уровень логирования
        result = add(2, 3)
        assert result == 5

    # Проверяем, что лог содержит информацию о начале и успешном завершении функции
    assert "add started with args: (2, 3), kwargs: {}" in caplog.text
    assert "add ok. Result: 5" in caplog.text


def test_divide_success(caplog: Any) -> None:
    """Тест для успешного выполнения функции divide с выводом в консоль."""
    with caplog.at_level(logging.INFO):
        result = divide(10, 2)
        assert result == 5.0

    # Проверяем, что лог содержит информацию о начале и успешном завершении функции
    assert "divide started with args: (10, 2), kwargs: {}" in caplog.text
    assert "divide ok. Result: 5.0" in caplog.text


def test_divide_error(caplog: Any) -> None:
    """Тест для обработки ошибки в функции divide с выводом в консоль."""
    with pytest.raises(ValueError, match="Division by zero"):
        with caplog.at_level(logging.INFO):
            divide(10, 0)

    # Проверяем, что лог содержит информацию о начале и ошибке
    assert "divide started with args: (10, 0), kwargs: {}" in caplog.text
    assert "divide error: ValueError. Inputs: (10, 0), {}" in caplog.text


def test_multiply_error_to_file(cleanup_log_file: Any) -> None:
    """Тест для обработки ошибки в функции multiply с логированием в файл."""

    @log(filename="test_log.txt")
    def faulty_function(x: int) -> None:
        raise RuntimeError("Something went wrong")

    with pytest.raises(RuntimeError, match="Something went wrong"):
        faulty_function(42)

    # Проверяем, что файл логов существует
    assert os.path.exists("test_log.txt")

    # Проверяем содержимое файла логов
    with open("test_log.txt", "r") as log_file:
        logs = log_file.read()
        assert "faulty_function started with args: (42,), kwargs: {}" in logs
        assert "faulty_function error: RuntimeError. Inputs: (42,), {}" in logs
