import base64
from http_basic_auth import parse_basic_auth_token, generate_basic_auth_token, BasicAuthTokenException


def test_token_parse():
    correct_token = str(base64.b64encode(b'test:secret'), encoding='ascii')
    assert parse_basic_auth_token(correct_token) == ('test', 'secret')

    with pytest.raises(BasicAuthTokenException):
        parse_basic_auth_token(None)

    with pytest.raises(BasicAuthTokenException):
        parse_basic_auth_token(True)

    with pytest.raises(BasicAuthTokenException):
        parse_basic_auth_token('+_)( not a base64 >< }{')

    with pytest.raises(BasicAuthTokenException):
        parse_basic_auth_token('Некорректный токен')

    incorrect_token = str(base64.b64encode(b'test_secret'), encoding='ascii')
    with pytest.raises(BasicAuthTokenException):
        parse_basic_auth_token(incorrect_token)


def test_token_gen():
    correct_token = str(base64.b64encode(b'test:secret'), encoding='ascii')
    assert correct_token == generate_basic_auth_token('test', 'secret')

    with pytest.raises(BasicAuthTokenException):
        generate_basic_auth_token('asd:qwe', 'password')

    with pytest.raises(BasicAuthTokenException):
        generate_basic_auth_token('Не', 'аски')
