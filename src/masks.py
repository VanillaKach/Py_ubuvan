def get_mask_card_number(card_number: str) -> str:
    """Маскировка номера банковской карты"""
    if len(card_number) == 16:
        mask_card_number: str = card_number.replace(card_number[6:12], "** **** ")
        mask_card_number = mask_card_number[:4] + " " + mask_card_number[4:]
        return mask_card_number
    elif not card_number.isdigit():
        return "Номер карты не указан!"
    elif len(card_number) != 16:
        return "Номер карты указан не верно!"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(bank_account_number: str) -> str:
    """Маскировка номера банковского счёта"""
    if len(bank_account_number) == 20:
        mask_account: str = bank_account_number.replace(bank_account_number[:-4], "**")
        return mask_account
    elif not bank_account_number.isdigit():
        return "Номер счёта не указан!"
    elif len(bank_account_number) != 20:
        return "Номер счёта указан не верно!"

print(get_mask_account("73654108430135874305"))
