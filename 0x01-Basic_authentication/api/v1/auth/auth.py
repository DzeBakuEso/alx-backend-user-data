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

        Args:
            path (str): The request path
            excluded_paths (List[str]): List of excluded (non-auth) paths

        Returns:
            bool: True if auth is required, False otherwise
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize path to always end with /
        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded.endswith('/') and path == excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Placeholder for getting the authorization header from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder for retrieving the current user
        """
        return None
