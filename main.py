from src.widget import mask_account_card

print(len("7000792289606361"))
print(len("84567895456212345784"))

result_card, result_account = mask_account_card("Visa Platinum 7000792289606361", "Счет 73654108430135874305")

print(result_card)
