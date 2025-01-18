import pytest

from src.widget import mask_account_card


@pytest.fixture
def number_card():
    return "Visa Platinum 7000792289606361", "Maestro 1596837868705199", "MasterCard 7158300734726758", "Visa Classic 6831982476737658", "Visa Gold 5999414228426353"

@pytest.fixture
def score_account():
    return "Счет 73654108430135874305"




@pytest.mark.parametrize("number_cards_and_score_account", "mask_card_number", [
    (("Visa Platinum 7000792289606361", "Счет 73654108430135874305"), ('Visa Platinum 7000 79** **** 6361', 'Счет **4305')),
    (("Maestro 1596837868705199", "Счет 64686473678894779589"), ('Maestro 1596 83** **** 5199', 'Счет **9589')),
    (("MasterCard 7158300734726758", "Счет 35383033474447895560"), ('MasterCard 7158 30** **** 6758', 'Счет **5560')),
    (("Visa Classic 6831982476737658", "Счет 73654108430135874305"), ('Visa Classic 6831 98** **** 7658', 'Счет **4305')),
    (("Visa Gold 5999414228426353", "Счет 84567895456212345784"), ('Visa Gold 5999 41** **** 6353', 'Счет **5784'))])
def test_mask_account_card(number_cards_and_score_account, mask_card_number):
    assert mask_account_card(number_cards_and_score_account) == mask_card_number