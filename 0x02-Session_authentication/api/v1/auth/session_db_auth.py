#!/usr/bin/env python3
"""
SessionDBAuth module - session authentication using database persistence.
"""

from typing import Optional
from uuid import uuid4
from models.user_session import UserSession
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """
    SessionDBAuth class: inherits from SessionExpAuth,
    stores sessions in database instead of memory.
    """

    def create_session(self, user_id: Optional[str] = None) -> Optional[str]:
        """
        Create a new session ID for a user and save it in the database.

        Args:
            user_id (str): User ID.

        Returns:
            str or None: Session ID or None if user_id is None.
        """
        if user_id is None:
            return None

        session_id = str(uuid4())
        # Create a new UserSession instance
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()  # Save to storage (file/db)
        return session_id

    def user_id_for_session_id(self, session_id: Optional[str] = None) -> Optional[str]:
        """
        Return user_id based on session_id from database.
        Also checks for session expiration as per SessionExpAuth.

        Args:
            session_id (str): Session ID.

        Returns:
            str or None: User ID or None if session_id invalid or expired.
        """
        if session_id is None:
            return None

        # Query all UserSession objects and filter by session_id
        sessions = UserSession.search({"session_id": session_id})
        if not sessions:
            return None

        user_session = sessions[0]

        # Check expiration if SESSION_DURATION is set
        if self.session_duration <= 0:
            return user_session.user_id

        from datetime import datetime, timedelta

        created_at = user_session.created_at
        if created_at is None:
            return None

        expire_time = created_at + timedelta(seconds=self.session_duration)
        if expire_time < datetime.now():
            return None

        return user_session.user_id

    def destroy_session(self, request=None) -> bool:
        """
        Delete UserSession object associated with session_id from request cookie.

        Args:
            request: Flask request object.

        Returns:
            bool: True if session destroyed, False otherwise.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        sessions = UserSession.search({"session_id": session_id})
        if not sessions:
            return False

        user_session = sessions[0]
        user_session.delete()
        return True
