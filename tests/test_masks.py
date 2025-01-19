import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_number() -> str:
    return "7000792289606361"


def test_get_card_number(card_number: str) -> None:
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


@pytest.fixture
def mask_account() -> str:
    return "22022065789536454568"


def test_get_mask_account(mask_account: str) -> None:
    assert get_mask_account(mask_account) == "**4568"


@pytest.mark.parametrize(
    "number_cards, mask_card_number",
    [
        ("2202202567899581", "2202 20** **** 9581"),
        ("2202206578953645", "2202 20** **** 3645"),
        ("21035468523145695654", "Номер карты указан не верно!"),
        ("24518462", "Номер карты указан не верно!"),
        ("", "Номер карты не указан!"),
    ],
)
def test_get_mask_card_number(number_cards: str, mask_card_number: str) -> None:
    assert get_mask_card_number(number_cards) == mask_card_number


@pytest.mark.parametrize(
    "mask_number, mask_account",
    [
        ("22022025678995814856", "**4856"),
        ("22022065789536454568", "**4568"),
        ("21035468523142555691354", "Номер счёта указан не верно!"),
        ("2451846294523", "Номер счёта указан не верно!"),
        ("", "Номер счёта не указан!"),
    ],
)
def test_get_mask_account_next(mask_number: str, mask_account: str) -> None:
    assert get_mask_account(mask_number) == mask_account
