#!/usr/bin/env python3
""" Main 4 """
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.extract_user_credentials(None))  # (None, None)
print(a.extract_user_credentials(89))  # (None, None)
print(a.extract_user_credentials("ALX"))  # (None, None)
print(a.extract_user_credentials("ALX:School"))  # ('ALX', 'School')
print(a.extract_user_credentials("bob@gmail.com:toto1234"))  # ('bob@gmail.com', 'toto1234')
