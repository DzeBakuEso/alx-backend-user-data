#!/usr/bin/env python3
""" SessionAuth module for session authentication
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a given user_id

        Args:
            user_id (str): ID of the user

        Returns:
            str: Session ID (UUID) or None if input invalid
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
