import logging

# Настройка логирования для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler("masks.log")
file_handler.setLevel(logging.DEBUG)

# Настройка форматирования логов
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскировка номера банковской карты"""
    logger.debug(f"Получен номер карты: {card_number}")

    if len(card_number) == 16 and card_number.isdigit():
        # Форматирование номера карты
        masked_part = "** **** "
        mask_card_number = f"{card_number[:4]} {card_number[4:6]}{masked_part}{card_number[12:]}"
        logger.info("Номер карты успешно замаскирован.")
        return mask_card_number
    elif not card_number:
        logger.error("Номер карты не указан!")
        return "Номер карты не указан!"
    elif len(card_number) != 16 or not card_number.isdigit():
        logger.error("Номер карты указан не верно!")
        return "Номер карты указан не верно!"
    else:
        logger.warning("Подумай и попробуй ещё раз ;)")
        return "Подумай и попробуй ещё раз ;)"


def get_mask_account(bank_account_number: str) -> str:
    """Маскировка номера банковского счёта"""
    logger.debug(f"Получен номер счета: {bank_account_number}")

    if len(bank_account_number) == 20 and bank_account_number.isdigit():
        mask_account = "**" + bank_account_number[-4:]  # Скрываем все, кроме последних 4 цифр
        logger.info("Номер счета успешно замаскирован.")
        return mask_account
    elif not bank_account_number:
        logger.error("Номер счета не указан!")
        return "Номер счёта не указан!"
    elif len(bank_account_number) != 20 or not bank_account_number.isdigit():
        logger.error("Номер счета указан не верно!")
        return "Номер счёта указан не верно!"
    else:
        logger.warning("Подумай и попробуй ещё раз ;)")
        return "Подумай и попробуй ещё раз ;)"


# Примеры использования функций
if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
