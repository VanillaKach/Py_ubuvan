from typing import Dict

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def filter_state() -> list[Dict]:  # Проверка функции на правильную фильтрацию
    return [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
    ]


def test_filter_by_state(filter_state: list[Dict]) -> None:
    assert filter_by_state(filter_state) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
    ]


@pytest.fixture
def filter_state_next() -> list[Dict]:  # Проверка функции на случай, если отсутствует параметр sate в словаре
    return [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T23:00:00.215544"},
        {"id": 123456789, "date": "2018-10-14T23:00:00.215544"},
        {"id": 987654321, "date": "2018-10-14T23:00:00.215544"},
    ]


def test_filter_by_state_next(filter_state_next: list[Dict]) -> None:
    assert filter_by_state(filter_state_next, "CANCELED") == [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T23:00:00.215544"},
    ]


@pytest.fixture
def no_sorted_date() -> list[Dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
        {"id": 15316, "state": "EXECUTED", "date": "2017-11-23T08:13:13.411257"},
        {"id": 215155444181, "state": "CANCELED", "date": "2003-05-06T08:12:46.212845"},
        {"id": 752135, "state": "EXECUTED", "date": "2002-01-01T08:21:19.369852"},
    ]


def test_no_sorted_date(no_sorted_date: list[Dict]) -> None:
    assert sort_by_date(no_sorted_date) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 15316, "state": "EXECUTED", "date": "2017-11-23T08:13:13.411257"},
        {"id": 215155444181, "state": "CANCELED", "date": "2003-05-06T08:12:46.212845"},
        {"id": 752135, "state": "EXECUTED", "date": "2002-01-01T08:21:19.369852"},
    ]
