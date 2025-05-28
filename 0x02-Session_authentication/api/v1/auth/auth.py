#!/usr/bin/env python3
"""Auth module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class for managing API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'
        for excluded in excluded_paths:
            if excluded.endswith('*'):
                if path.startswith(excluded[:-1]):
                    return False
            elif path == excluded:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the value of the Authorization header"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Placeholder for current user (to be overridden)"""
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""
        if request is None:
            return None
        return request.cookies.get('_my_session_id')

    def extract_base64_authorization_header(self, auth_header: str) -> str:
        """Extracts the Base64 part of the Authorization header"""
        if auth_header is None or not isinstance(auth_header, str):
            return None
        if not auth_header.startswith("Basic "):
            return None
        return auth_header.split(" ", 1)[1]
