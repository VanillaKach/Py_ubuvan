

print(len("7000792289606361"))
print(len("84567895456212345784"))

#result_card, result_account = mask_account_card("Visa Platinum 7000792289606361", "Счет 73654108430135874305")

#print(result_card)

def mask_account_card(number_card_or_score_account: str):
    """Функция для маскировки номера банковской карты и банковского счёта"""
    return number_card_or_score_account.split(" ")[-1]


print(mask_account_card("Visa Platinum 7000792289606361"))




