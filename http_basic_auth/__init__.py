"""
HTTP Basic Auth python lib
"""

import base64
from typing import Tuple


class BasicAuthException(Exception):
    """General exception for all http-basic-auth problems
    """


def parse_token(token: str, coding='utf-8') -> Tuple[str, str]:
    """Get login + password tuple from Basic Auth token.
    """
    try:
        token_as_bytes = bytes(token, encoding=coding)
    except UnicodeEncodeError as exc:
        raise BasicAuthException from exc
    except TypeError as exc:
        raise BasicAuthException from exc

    try:
        auth_pair = base64.b64decode(token_as_bytes, validate=True)
    except base64.binascii.Error as exc:
        raise BasicAuthException from exc

    try:
        login, password = auth_pair.split(b':', maxsplit=1)
    except ValueError as exc:
        raise BasicAuthException from exc

    try:
        return str(login, encoding=coding), str(password, encoding=coding)
    except UnicodeDecodeError as exc:
        raise BasicAuthException from exc


def generate_token(login: str, password: str, coding='utf-8') -> str:
    """Generate Basic Auth token from login and password
    """
    try:
        login_as_bytes = bytes(login, encoding=coding)
        password_as_bytes = bytes(password, encoding=coding)
    except UnicodeEncodeError as exc:
        raise BasicAuthException from exc
    except TypeError as exc:
        raise BasicAuthException from exc

    if b':' in login_as_bytes:
        raise BasicAuthException

    token: bytes = base64.b64encode(
        b'%b:%b' % (login_as_bytes, password_as_bytes)
    )

    return str(token, encoding=coding)


def parse_header(header_value: str, coding='utf-8') -> Tuple[str, str]:
    """Get login + password tuple from Basic Auth header value.
    """
    if header_value is None:
        raise BasicAuthException

    try:
        basic_prefix, token = header_value.strip().split(maxsplit=1)
    except AttributeError as exc:
        raise BasicAuthException from exc
    except ValueError as exc:
        raise BasicAuthException from exc

    if basic_prefix.lower() != 'basic':
        raise BasicAuthException

    return parse_token(token, coding=coding)


def generate_header(login: str, password: str, coding='utf-8') -> str:
    """Generate Basic Auth header value from login and password
    """
    return 'Basic %s' % generate_token(login, password, coding=coding)
