import pytest

from http_basic_auth import parse_token, generate_token, BasicAuthException


@pytest.mark.parametrize("token,expect", [
    ('dGVzdDpzZWNyZXQ=', ('test', 'secret')),
    ('dGVzdDpzZWNyZXQx', ('test', 'secret1')),
    ('dGVzdDpzZWM6cmV0MQ==', ('test', 'sec:ret1')),
    ('bmFtZTp9e3NkYXNkJyI=', ('name', '}{sdasd\'\"')),
])
def test_token_parse(token, expect):
    assert parse_token(token, coding='ascii') == expect


@pytest.mark.parametrize("token", [
    ('dGVzdDp}{zZWNyZXQ=',),  # not base64 symbols
    (None,),
    (True,),
    ('тест®',),     # non-latin
    ('dGVzdA==',),  # no ":" in encoded string
    ('8J+YgTrQv9Cw0YA6w7bQu9GM',),  # utf8 inside
])
def test_wrong_token_parse(token):
    with pytest.raises(BasicAuthException):
        parse_token(token, coding='ascii')


@pytest.mark.parametrize("token,login_password", [
    ('dGVzdDpzZWNyZXQ=', ('test', 'secret')),
    ('dGVzdDpzZWNyZXQx', ('test', 'secret1')),
    ('dGVzdDpzZWM6cmV0MQ==', ('test', 'sec:ret1')),
    ('bmFtZTp9e3NkYXNkJyI=', ('name', '}{sdasd\'\"')),
])
def test_token_gen(token, login_password):
    assert token == generate_token(*login_password, coding='ascii')


@pytest.mark.parametrize("login_password", [
    ('te:st', 'secret'),
    ('Не', 'аски'),
    (True, 'sec:ret1'),
    (None, 'sec:ret1'),
    ('test', True),
    ('test', None),
])
def test_wrong_token_gen(login_password):
    with pytest.raises(BasicAuthException):
        generate_token(*login_password, coding='ascii')
