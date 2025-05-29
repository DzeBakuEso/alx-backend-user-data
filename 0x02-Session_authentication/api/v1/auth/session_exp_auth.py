#!/usr/bin/env python3
"""
SessionExpAuth module that inherits from SessionAuth
and adds session expiration capability.
"""

from os import getenv
from datetime import datetime, timedelta
from typing import Optional
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """
    SessionExpAuth inherits from SessionAuth and adds
    expiration time to sessions.
    """

    def __init__(self) -> None:
        """
        Initialize SessionExpAuth instance.

        Assign session_duration from environment variable SESSION_DURATION.
        If not set or invalid, assign 0 (no expiration).
        """
        super().__init__()
        try:
            self.session_duration = int(getenv("SESSION_DURATION", 0))
        except (ValueError, TypeError):
            self.session_duration = 0

    def create_session(self, user_id: Optional[str] = None) -> Optional[str]:
        """
        Create a Session ID for user_id and store
        created_at timestamp.

        Args:
            user_id (str): user identifier

        Returns:
            str: Session ID if created, else None
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        # Overwrite the session data with dictionary holding user_id and created_at
        self.user_id_by_session_id[session_id] = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id: Optional[str] = None) -> Optional[str]:
        """
        Return user_id if session valid and not expired.

        Args:
            session_id (str): session ID

        Returns:
            str: user_id if session valid
            None: if session_id invalid, expired, or no user_id found
        """
        if session_id is None:
            return None

        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None or not isinstance(session_dict, dict):
            return None

        user_id = session_dict.get("user_id")
        created_at = session_dict.get("created_at")

        if user_id is None or created_at is None:
            return None

        if self.session_duration <= 0:
            return user_id

        # Check expiration
        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if datetime.now() > expiration_time:
            return None

        return user_id
