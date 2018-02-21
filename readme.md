# http-basic-auth


Yep, it's one more HTTP Basic Auth python lib. The second. And I tried
to use the first, but it had a bug (which I fixed) and... completely
wrong realisation of non-latin encoding/decoding.

Also it supports only RFC-2617, but RFC-7617 is actual.

I want to implement full HTTP Basic Auth protocol, but I'll start from
RFC-2617 version.

# Install

```bash
pip3 install http-basic-auth
```

# ♥️ Non-latin symbols

http-basic-auth ♥ utf-8

```bash
→ curl --user name:пароль https://httpbin.org/headers
{
  "headers": {
    "Accept": "*/*", 
    "Authorization": "Basic bmFtZTrQv9Cw0YDQvtC70Yw=", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "curl/7.54.0"
  }
}
```

And even

```bash
→ curl --user 😁:пар:öль https://httpbin.org/headers
{
  "headers": {
    "Accept": "*/*", 
    "Authorization": "Basic 8J+YgTrQv9Cw0YA6w7bQu9GM", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "curl/7.54.0"
  }
}
```

All it works fine, if you define your charset

```python
from http_basic_auth import generate_header, parse_header


assert "Basic 8J+YgTrQv9Cw0YA6w7bQu9GM" == generate_header('😁', 'пар:öль', coding='utf-8')
assert ('😁', 'пар:öль') == parse_header("Basic 8J+YgTrQv9Cw0YA6w7bQu9GM", coding='utf-8')
```

# Provides functions

- `generate_header`: `(user, password) → "Basic <token>"`
- `parse_header`: `"Basic <token>" → (user, password)`
- `generate_token`: `(user, password) → "<token>"`
- `parse_token`: `"<token>" → (user, password)`
