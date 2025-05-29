#!/usr/bin/env python3
"""
Session authentication module
"""

from typing import List, Optional
import uuid


class Auth:
    """Base Auth class"""

    def require_auth(self, path: Optional[str], excluded_paths: Optional[List[str]]) -> bool:
        """
        Determines if a route requires authentication.

        Args:
            path (str): The requested path
            excluded_paths (list): List of paths excluded from auth

        Returns:
            bool: True if auth required, False otherwise
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Ensure slash tolerance: path and excluded_paths end with '/'
        if path[-1] != '/':
            path += '/'

        for ep in excluded_paths:
            if ep[-1] != '/':
                ep += '/'
            if ep == path:
                return False
        return True


class SessionAuth(Auth):
    """Session authentication class"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str) -> Optional[str]:
        """Create a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str) -> Optional[str]:
        """Return the user_id linked to a session_id"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def session_cookie(self, request=None) -> Optional[str]:
        """Retrieve session ID from cookie in request"""
        if request is None:
            return None
        cookie_name = self.session_cookie_name()
        if cookie_name is None:
            return None
        return request.cookies.get(cookie_name)

    def session_cookie_name(self) -> str:
        """
        Return the name of the session cookie
        This should match your ENV variable SESSION_NAME or default
        """
        from os import getenv

        session_name = getenv("SESSION_NAME")
        if session_name is None:
            session_name = "_my_session_id"  # default name
        return session_name

    def destroy_session(self, request=None) -> bool:
        """
        Deletes the user session / logout

        Args:
            request (flask.Request): request object

        Returns:
            bool: True if session deleted, False otherwise
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        # Delete the session_id key to logout
        try:
            del self.user_id_by_session_id[session_id]
            return True
        except KeyError:
            return False
