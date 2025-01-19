def mask_account_card(number_card_or_score_account: str) -> str:
    """Функция для маскировки номера банковской карты и банковского счёта"""
    if len(number_card_or_score_account.split(" ")[-1]) == 16:
        for number in number_card_or_score_account.split():  # маскировка номера карты
            if number.isdigit():
                number = number.replace(number[6:12], "** **** ")
                result_number = number[:4] + " " + number[4:]
            else:
                pass
        mask_card = number_card_or_score_account.replace(number_card_or_score_account[-16:], result_number)
        return mask_card
    elif len(number_card_or_score_account.split(" ")[-1]) == 20:
        mask_score_account = number_card_or_score_account.replace(number_card_or_score_account[:-4], "**")

        for score in number_card_or_score_account.split():  # маскировка номера счёта
            if number_card_or_score_account.isdigit():
                mask_score_account = score.replace(score[:-4], "**")
            else:
                pass
        mask_account = number_card_or_score_account.replace(number_card_or_score_account[-20:], mask_score_account)
        return mask_account
    else:
        return "Номер карты или счёта указан не верно!"


print(mask_account_card("Счет 73654108430135874305"))
# Visa Platinum 7000792289606361
# Счет 73654108430135874305


def get_date(old_date: str) -> str:
    """Функция для переформатирования даты в формате 'дд.мм.гггг'"""
    if len(old_date) == 26:
        year = old_date[0:4]
        month = old_date[5:7]
        day = old_date[8:10]
        new_date = f"{day}.{month}.{year}"
        return new_date
    else:
        return "Дата указана не верно!"


print(get_date("2024-03-11T02:26:18.671407"))
