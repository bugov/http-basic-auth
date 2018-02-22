import pytest

from http_basic_auth import parse_header, generate_header, BasicAuthException


@pytest.mark.parametrize("token,expect", [
    ('Basic dGVzdDpzZWNyZXQ=', ('test', 'secret')),
    ('BASIC dGVzdDpzZWNyZXQx', ('test', 'secret1')),
    ('BaSiC dGVzdDpzZWM6cmV0MQ==', ('test', 'sec:ret1')),
    ('Basic    \t bmFtZTp9e3NkYXNkJyI=', ('name', '}{sdasd\'\"')),
    ('Basic 8J+YgTrQv9Cw0YA6w7bQu9GM', ('😁', 'пар:öль')),
])
def test_header_parse(token, expect):
    assert parse_header(token, coding='utf-8') == expect


@pytest.mark.parametrize("header", [
    '',
    'BasicdGVzdDpzZWNyZXQ=',
    'BASI dGVzdDpzZWNyZXQx',
    'dGVzdDpzZWM6cmV0MQ==',
    None,
    1,
])
def test_wrong_header_parse(header):
    with pytest.raises(BasicAuthException):
        parse_header(header, coding='utf-8')


@pytest.mark.parametrize("token,login_password", [
    ('Basic dGVzdDpzZWNyZXQ=', ('test', 'secret')),
    ('Basic dGVzdDpzZWNyZXQx', ('test', 'secret1')),
    ('Basic dGVzdDpzZWM6cmV0MQ==', ('test', 'sec:ret1')),
    ('Basic bmFtZTp9e3NkYXNkJyI=', ('name', '}{sdasd\'\"')),
    ('Basic 8J+YgTrQv9Cw0YA6w7bQu9GM', ('😁', 'пар:öль')),
])
def test_header_gen(token, login_password):
    assert token == generate_header(*login_password, coding='utf-8')


@pytest.mark.parametrize("token,expect", [
    ('Basic 8J+YgTrQv9Cw0YA6w7bQu9GM', ('😁', 'пар:öль')),
])
def test_header_parse_utf8_default(token, expect):
    assert parse_header(token) == expect


@pytest.mark.parametrize("token,login_password", [
    ('Basic 8J+YgTrQv9Cw0YA6w7bQu9GM', ('😁', 'пар:öль')),
])
def test_header_gen_utf8_default(token, login_password):
    assert token == generate_header(*login_password)
