#!/usr/bin/env python3
"""
Authentication module
"""

from db import DB
import bcrypt
from user import User


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """
        Hash a password using bcrypt.

        Args:
            password (str): Password string.

        Returns:
            bytes: Hashed password.
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with email and password.

        Args:
            email (str): User email.
            password (str): Plain password.

        Returns:
            User: The newly created User object.

        Raises:
            ValueError: If user with email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            # If no exception, user already exists
            raise ValueError(f"User {email} already exists")
        except Exception:
            # User does not exist, safe to create
            pass

        hashed_pwd = self._hash_password(password)
        return self._db.add_user(email, hashed_pwd)
