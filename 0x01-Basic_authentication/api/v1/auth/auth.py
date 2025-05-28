#!/usr/bin/env python3
""" Auth class for API authentication
"""

from typing import List
from flask import request


class Auth:
    """Template for all authentication system classes"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a given path requires authentication.

        - Returns False if path is in excluded_paths
        - Supports wildcard '*' at the end of excluded paths for prefix matching
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # Normalize path by ensuring it ends with '/'
        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded.endswith('*'):
                # Match prefix if wildcard present
                if path.startswith(excluded[:-1]):
                    return False
            else:
                # Normalize excluded path
                if not excluded.endswith('/'):
                    excluded += '/'
                if path == excluded:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """Retrieve Authorization header from request"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None):
        """Get current authenticated user (to be implemented in child class)"""
        return None
