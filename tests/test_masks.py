import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_number():
    return "7000792289606361"

@pytest.mark.parametrize("number_cards, mask_card_number", [
    ("2202202567899581", "2202 20** **** 9581"),
    ("2202206578953645", "2202 20** **** 3645"),
    ("2103546852314569", "2103 54** **** 4569"),
    ("2451846297846532", "2451 84** **** 6532"),
    ("5124567894513256", "5124 56** **** 3256")])
def test_get_mask_card_number(number_cards, mask_card_number):
    assert get_mask_card_number(number_cards) == mask_card_number


@pytest.mark.parametrize("mask_number, mask_account", [
    ("22022025678995814856", "**4856"),
    ("22022065789536454568", "**4568"),
    ("21035468523145691354", "**1354"),
    ("24518462978465324523", "**4523"),
    ("51245678945132564597", "**4597")])
def test_get_mask_account(mask_number, mask_account):
    assert get_mask_account(mask_number) == mask_account
