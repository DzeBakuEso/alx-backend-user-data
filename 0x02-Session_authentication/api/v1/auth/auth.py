#!/usr/bin/env python3
"""Auth module
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Auth class for managing the authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path."""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        for ex_path in excluded_paths:
            if ex_path.endswith('*'):
                if path.startswith(ex_path[:-1]):
                    return False
            elif ex_path == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request."""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user (to be implemented later)."""
        return None

    def session_cookie(self, request=None):
        """
        Returns the value of the session cookie from a request.
        The name of the cookie is defined by the env variable SESSION_NAME.
        """
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        if session_name is None:
            return None
        return request.cookies.get(session_name)
