import pytest

from utils import get_data, get_filtered_data, get_last_values, get_formatted_data, encode_bill_info

def test_get_data():
    data = get_data()
    assert isinstance(data, list)

def test_get_filtered_data(test_data):
    data = get_filtered_data(test_data)
    assert len(data) == 3

def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert [x["date"] for x in data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2019-04-04T23:20:05.206878', '2019-03-23T01:09:46.296404']

def test_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.88 руб.']


@pytest.parametrize("test_input, expected", [
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Platinum 1596837868705199", "Visa Platinum 1596 83** **** 5199")
])


def test_encoding_bill_info(test_input, expected):
    assert encode_bill_info(test_input) == expected

