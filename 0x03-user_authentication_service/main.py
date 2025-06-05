#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.valid_login(email, password))         # True
print(auth.valid_login(email, "WrongPwd"))       # False
print(auth.valid_login("unknown@email", password))  # False
