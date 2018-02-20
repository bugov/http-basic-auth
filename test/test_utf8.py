import pytest

from http_basic_auth import parse_basic_auth_token, generate_basic_auth_token, BasicAuthTokenException


@pytest.mark.parametrize("token,expect", [
    ('bmFtZTrQv9Cw0YDQvtC70Yw=', ('name', 'пароль')),
    ('bmFtZTrQv9Cw0YA60L7Qu9GM', ('name', 'пар:оль')),
    ('8J+YgTrQv9Cw0YA6w7bQu9GM', ('😁', 'пар:öль')),
])
def test_token_parse(token, expect):
    assert parse_basic_auth_token(token, coding='utf-8') == expect


@pytest.mark.parametrize("token,login_password", [
    ('bmFtZTrQv9Cw0YDQvtC70Yw=', ('name', 'пароль')),
    ('bmFtZTrQv9Cw0YA60L7Qu9GM', ('name', 'пар:оль')),
    ('8J+YgTrQv9Cw0YA6w7bQu9GM', ('😁', 'пар:öль')),
])
def test_token_gen(token, login_password):
    assert token == generate_basic_auth_token(*login_password, coding='utf-8')
