import base64

import pytest

from http_basic_auth import parse_basic_auth_token, generate_basic_auth_token, BasicAuthTokenException


@pytest.mark.parametrize("token,expect", [
    ('dGVzdDpzZWNyZXQ=', ('test', 'secret')),
    ('dGVzdDpzZWNyZXQx', ('test', 'secret1')),
    ('dGVzdDpzZWM6cmV0MQ==', ('test', 'sec:ret1')),
])
def test_token_parse(token, expect):
    assert parse_basic_auth_token(token) == expect


@pytest.mark.parametrize("token", [
    ('dGVzdDp}{zZWNyZXQ=',),  # not base64 symbols
    (None,),
    (True,),
    ('тест®',),     # non-latin
    ('dGVzdA==',),  # no ":" in encoded string
])
def test_wrong_token_parse(token):
    with pytest.raises(BasicAuthTokenException):
        parse_basic_auth_token(token)


@pytest.mark.parametrize("token,login_password", [
    ('dGVzdDpzZWNyZXQ=', ('test', 'secret')),
    ('dGVzdDpzZWNyZXQx', ('test', 'secret1')),
    ('dGVzdDpzZWM6cmV0MQ==', ('test', 'sec:ret1')),
])
def test_token_gen(token, login_password):
    assert token == generate_basic_auth_token(*login_password)


@pytest.mark.parametrize("login_password", [
    ('te:st', 'secret'),
    ('Не', 'аски'),
    (True, 'sec:ret1'),
    (None, 'sec:ret1'),
    ('test', True),
    ('test', None),
])
def test_wrong_token_gen(login_password):
    with pytest.raises(BasicAuthTokenException):
        generate_basic_auth_token(*login_password)