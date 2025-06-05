#!/usr/bin/env python3
"""Test create_session."""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

try:
    auth.register_user(email, password)
except ValueError:
    print(f"User {email} already exists")

print(auth.create_session(email))
print(auth.create_session("unknown@email.com"))
