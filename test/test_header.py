import pytest

from http_basic_auth import parse_basic_auth_header, generate_basic_auth_header, BasicAuthTokenException


@pytest.mark.parametrize("token,expect", [
    ('Basic dGVzdDpzZWNyZXQ=', ('test', 'secret')),
    ('BASIC dGVzdDpzZWNyZXQx', ('test', 'secret1')),
    ('BaSiC dGVzdDpzZWM6cmV0MQ==', ('test', 'sec:ret1')),
    ('Basic    \t bmFtZTp9e3NkYXNkJyI=', ('name', '}{sdasd\'\"')),
    ('Basic 8J+YgTrQv9Cw0YA6w7bQu9GM', ('😁', 'пар:öль')),
])
def test_header_parse(token, expect):
    assert parse_basic_auth_header(token, coding='utf-8') == expect


@pytest.mark.parametrize("token", [
    ('BasicdGVzdDpzZWNyZXQ=',),
    ('BASI dGVzdDpzZWNyZXQx',),
    ('dGVzdDpzZWM6cmV0MQ==',),
    (None,),
])
def test_wrong_header_parse(token):
    with pytest.raises(BasicAuthTokenException):
        parse_basic_auth_header(token, coding='utf-8')


@pytest.mark.parametrize("token,login_password", [
    ('Basic dGVzdDpzZWNyZXQ=', ('test', 'secret')),
    ('Basic dGVzdDpzZWNyZXQx', ('test', 'secret1')),
    ('Basic dGVzdDpzZWM6cmV0MQ==', ('test', 'sec:ret1')),
    ('Basic bmFtZTp9e3NkYXNkJyI=', ('name', '}{sdasd\'\"')),
    ('Basic 8J+YgTrQv9Cw0YA6w7bQu9GM', ('😁', 'пар:öль')),
])
def test_header_gen(token, login_password):
    assert token == generate_basic_auth_header(*login_password, coding='utf-8')
