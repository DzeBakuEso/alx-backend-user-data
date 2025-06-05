#!/usr/bin/env python3
"""Authentication helper module."""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class that proxies DB operations."""

    def __init__(self) -> None:
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """
        Hash a password with bcrypt.

        Args:
            password (str): Plain password.

        Returns:
            bytes: Salted bcrypt hash.
        """
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.

        Raises:
            ValueError: If email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except Exception:
            pass

        hashed_pwd = self._hash_password(password)
        return self._db.add_user(email, hashed_pwd)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate a user's login credentials.

        Args:
            email (str): Email address.
            password (str): Plain text password.

        Returns:
            bool: True if credentials match, else False.
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode("utf-8"),
                              user.hashed_password):
                return True
            return False
        except Exception:
            return False
