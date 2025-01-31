import functools
import logging
from typing import Any, Callable, Optional, TypeVar, Union

R = TypeVar("R")


def log(filename: Optional[str] = None) -> Callable[[Callable[..., R]], Callable[..., R]]:
    def decorator(func: Callable[..., R]) -> Callable[..., R]:
        # Настраиваем логгер
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)

        # Если указан файл, записываем логи в файл, иначе в консоль
        handler: Union[logging.FileHandler, logging.StreamHandler]

        if filename:
            handler = logging.FileHandler(filename)
        else:
            handler = logging.StreamHandler()

        # Устанавливаем формат логов
        formatter = logging.Formatter("%(asctime)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> R:
            # Логируем начало работы функции
            logger.info(f"{func.__name__} started with args: {args}, kwargs: {kwargs}")
            try:
                # Выполняем функцию
                result = func(*args, **kwargs)
                # Логируем успешное выполнение
                logger.info(f"{func.__name__} ok. Result: {result}")
                return result
            except Exception as e:
                # Логируем ошибку
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise  # Пробрасываем исключение дальше

        return wrapper

    return decorator
