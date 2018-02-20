import base64

__version__ = '0.1.0'


class BasicAuthTokenException(Exception):
    pass


def parse_basic_auth_token(token: str, coding='ascii') -> (str, str):
    """
    Get login + password tuple from Basic Auth token.
    """
    try:
        b_token = bytes(token, encoding=coding)
    except UnicodeEncodeError as e:
        raise BasicAuthTokenException from e
    except TypeError as e:
        raise BasicAuthTokenException from e

    try:
        auth_pair = base64.b64decode(b_token)
    except base64.binascii.Error as e:
        raise BasicAuthTokenException from e

    try:
        (login, password) = auth_pair.split(b':', maxsplit=1)
    except ValueError as e:
        raise BasicAuthTokenException from e

    return str(login, encoding=coding), str(password, encoding=coding)


def generate_basic_auth_token(login: str, password: str, coding='ascii') -> str:
    """
    Generate Basic Auth token from login and password
    """
    try:
        b_login = bytes(login, encoding=coding)
        b_password = bytes(password, encoding=coding)
    except UnicodeEncodeError as e:
        raise BasicAuthTokenException from e
    except TypeError as e:
        raise BasicAuthTokenException from e

    if b':' in b_login:
        raise BasicAuthTokenException

    b_token = base64.b64encode(b'%b:%b' % (b_login, b_password))

    return str(b_token, encoding=coding)
