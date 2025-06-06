#!/usr/bin/env python3
""" Main 3 """
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.decode_base64_authorization_header(None))  # None
print(a.decode_base64_authorization_header(89))  # None
print(a.decode_base64_authorization_header("ALX"))  # None
print(a.decode_base64_authorization_header("SG9sYmVydG9u"))  # Holberton
print(a.decode_base64_authorization_header("SG9sYmVydG9uIFNjaG9vbA=="))  # Holberton School
print(a.decode_base64_authorization_header(
    a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA==")
))  # Holberton School
