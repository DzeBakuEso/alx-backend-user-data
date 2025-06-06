#!/usr/bin/env python3
"""Auth class methods for user authentication"""

import uuid
from typing import Optional
from db import DB  # Assuming DB class is your database interface
from user import User  # Assuming User is your user model
from bcrypt import hashpw, gensalt


class Auth:
    def __init__(self):
        self._db = DB()

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update user's password using reset token.

        Args:
            reset_token (str): The reset password token.
            password (str): The new password.

        Raises:
            ValueError: If no user found with the reset token.
        """
        if not reset_token or not password:
            raise ValueError("reset_token and password must be provided")

        user = self._db.find_user_by(reset_token=reset_token)
        if user is None:
            raise ValueError("Invalid reset token")

        # Hash the new password
        hashed = self._hash_password(password)

        # Update user's hashed_password and reset_token fields
        self._db.update_user(user.id, hashed_password=hashed, reset_token=None)

    def _hash_password(self, password: str) -> str:
        """Return the bcrypt hash of the password."""
        hashed = hashpw(password.encode('utf-8'), gensalt())
        return hashed.decode('utf-8')
