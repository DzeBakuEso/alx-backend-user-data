#!/usr/bin/env python3
"""
Auth class to manage API authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class template for authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a path requires authentication
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded.endswith('/') and path == excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Gets the Authorization header from the request
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder for retrieving the current user
        """
        return None
