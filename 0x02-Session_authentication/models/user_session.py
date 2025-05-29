#!/usr/bin/env python3
"""
UserSession model - stores session_id and user_id in persistent storage.
"""

from models.base import BaseModel


class UserSession(BaseModel):
    """
    UserSession class: stores user_id and session_id.

    Attributes:
        user_id (str): ID of the user.
        session_id (str): Session ID.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        Initialize UserSession with user_id and session_id.

        Args:
            user_id (str): User identifier.
            session_id (str): Session identifier.
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get("user_id")
        self.session_id = kwargs.get("session_id")
