#!/usr/bin/env python3
"""Authentication module"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a randomly-generated salt.

    Args:
        password (str): The password string to hash.

    Returns:
        bytes: The salted hash of the password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
