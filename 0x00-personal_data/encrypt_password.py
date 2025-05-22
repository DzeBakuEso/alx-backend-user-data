#!/usr/bin/env python3
"""
encrypt_password.py
Provides password hashing using bcrypt with salt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with a salt.
    
    Args:
        password (str): The plaintext password to hash.
        
    Returns:
        bytes: The salted, hashed password as a byte string.
    """
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    # Generate salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed
