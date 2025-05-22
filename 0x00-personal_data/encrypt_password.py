#!/usr/bin/env python3
"""
Encryption utilities for password hashing and validation using bcrypt.
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """Hash a password with a salt and return the hashed byte string."""
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate a plaintext password against the stored hashed password.

    Args:
        hashed_password (bytes): The hashed password to check against.
        password (str): The plaintext password to verify.

    Returns:
        bool: True if password matches the hashed password, False otherwise.
    """
    if not isinstance(hashed_password, bytes):
        raise TypeError("hashed_password must be bytes")
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
