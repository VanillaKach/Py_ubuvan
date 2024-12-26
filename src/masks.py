def get_mask_card_number(card_number: str):
    """Маскировка номера банковской карты"""
    mask_card_number: str = card_number.replace(card_number[6:12], "** **** ")
    mask_card_number = mask_card_number[:4] + " " + mask_card_number[4:]
    return mask_card_number


print(get_mask_card_number("7000792289606361"))


def get_mask_account(bank_account_number: str):
    """Маскировка номера банковского счёта"""
    mask_account: str = bank_account_number.replace(bank_account_number[:-4], "**")
    return mask_account


print(get_mask_account("73654108430135874305"))

# Сделал именно таким образом и без цикла, потому что номер счёта всегда будет иметь одинаковую длину,
# что позволяет использовать срезы. Аналогично работает с номером карты.
