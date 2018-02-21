import pytest

from http_basic_auth import parse_token, generate_token


@pytest.mark.parametrize("token,expect", [
    ('bmFtZTrQv9Cw0YDQvtC70Yw=', ('name', 'пароль')),
    ('bmFtZTrQv9Cw0YA60L7Qu9GM', ('name', 'пар:оль')),
    ('8J+YgTrQv9Cw0YA6w7bQu9GM', ('😁', 'пар:öль')),
])
def test_token_parse(token, expect):
    assert parse_token(token, coding='utf-8') == expect


@pytest.mark.parametrize("token,login_password", [
    ('bmFtZTrQv9Cw0YDQvtC70Yw=', ('name', 'пароль')),
    ('bmFtZTrQv9Cw0YA60L7Qu9GM', ('name', 'пар:оль')),
    ('8J+YgTrQv9Cw0YA6w7bQu9GM', ('😁', 'пар:öль')),
])
def test_token_gen(token, login_password):
    assert token == generate_token(*login_password, coding='utf-8')


@pytest.mark.parametrize("token,expect", [
    ('8J+YgTrQv9Cw0YA6w7bQu9GM', ('😁', 'пар:öль')),
])
def test_utf8_default_parse(token, expect):
    assert parse_token(token) == expect


@pytest.mark.parametrize("token,login_password", [
    ('8J+YgTrQv9Cw0YA6w7bQu9GM', ('😁', 'пар:öль')),
])
def test_utf8_default_gen(token, login_password):
    assert token == generate_token(*login_password)
