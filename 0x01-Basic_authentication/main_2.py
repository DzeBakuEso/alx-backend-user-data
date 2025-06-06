#!/usr/bin/env python3
""" Main 2 """
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.extract_base64_authorization_header(None))  # None
print(a.extract_base64_authorization_header(89))  # None
print(a.extract_base64_authorization_header("ALX"))  # None
print(a.extract_base64_authorization_header("Basic ALX"))  # ALX
print(a.extract_base64_authorization_header("Basic SG9sYmVydG9u"))  # SG9sYmVydG9u
print(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA=="))  # SG9sYmVydG9uIFNjaG9vbA==
print(a.extract_base64_authorization_header("Basic1234"))  # None
