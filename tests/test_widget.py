import pytest

from src.widget import mask_account_card, get_date


# Тестирование функции mask_account_card, если на вход идёт номер карты
@pytest.fixture
def number_card():
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def mask_number_card():
    return "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card(number_card, mask_number_card):
    assert mask_account_card(number_card) == mask_number_card


# Тестирование функции mask_account_card, если на вход идёт номер счёта
@pytest.fixture
def score_account():
    return "Счет 73654108430135874305"


@pytest.fixture
def mask_score_account():
    return "Счет **4305"


def test_mask_account_score(score_account, mask_score_account):
    assert mask_account_card(score_account) == mask_score_account


# Тестирование функции mask_account_card, если на вход идёт номер карты
@pytest.mark.parametrize(
    "number_card, mask_card_number",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300731155531351324726758", "Номер карты или счёта указан не верно!"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Gold 5941353", "Номер карты или счёта указан не верно!"),
    ],
)
def test_mask_account_cards(number_card, mask_card_number):
    assert mask_account_card(number_card) == mask_card_number


# Тестирование функции mask_account_card, если на вход идёт номер счёта
@pytest.mark.parametrize(
    "number_score, mask_score_account",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 736541084301351553111488874305", "Номер карты или счёта указан не верно!"),
        ("Счет 845645784", "Номер карты или счёта указан не верно!"),
    ],
)
def test_mask_account_score(number_score, mask_score_account):
    assert mask_account_card(number_score) == mask_score_account


# Тестирование функции get_date
@pytest.fixture
def no_format_date():
    return "2024-03-11T02:26:18.671407"


def test_get_date(no_format_date):
    assert get_date(no_format_date) == "11.03.2024"


@pytest.mark.parametrize(
    "date_not_format, good_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-06-05T02:22:11.548621", "05.06.2025"),
        ("2025-01-01T02:24:14.654987", "01.01.2025"),
        ("2025-03-08T02:27:13.3", "Дата указана не верно!"),
        ("20234-102-13T02:201:19.6564545123", "Дата указана не верно!"),
    ],
)
def test_get_date(date_not_format, good_date):
    assert get_date(date_not_format) == good_date
