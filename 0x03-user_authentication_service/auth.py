#!/usr/bin/env python3
"""Auth module"""
import uuid
from typing import Optional
from db import DB
from user import User


class Auth:
    """Auth class to manage the authentication process"""

    def __init__(self):
        self._db = DB()

    # Other methods here ...

    def get_reset_password_token(self, email: str) -> str:
        """Generate a reset password token for user with email

        Args:
            email (str): The user's email address

        Returns:
            str: The generated reset password token

        Raises:
            ValueError: If no user found with the email
        """
        user = self._db.find_user_by(email=email)
        if user is None:
            raise ValueError(f"No user found for email: {email}")

        reset_token = str(uuid.uuid4())
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token
