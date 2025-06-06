#!/usr/bin/env python3
"""Auth module for handling user authentication
"""
import bcrypt
from db import DB
from user import User
from uuid import uuid4
from typing import Optional


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user with hashed password.
        Raises:
            ValueError: If user already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except Exception:
            hashed_pwd = _hash_password(password)
            return self._db.add_user(email, hashed_pwd)

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user's login credentials.
        Returns True if password matches, else False.
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode(), user.hashed_password):
                return True
        except Exception:
            pass
        return False

    def create_session(self, email: str) -> Optional[str]:
        """Creates a session ID for a user and stores it.
        Returns the session ID or None if user not found.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = self._generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """Returns the user associated with the session ID.
        Returns None if session ID is invalid or user not found.
        """
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys the session by setting the session_id to None."""
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception:
            pass

    def _generate_uuid(self) -> str:
        """Generates a new UUID string."""
        return str(uuid4())


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt with salt.
    Returns:
        bytes: The hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
