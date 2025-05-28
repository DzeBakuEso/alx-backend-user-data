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
        Returns False for now, to be implemented later

        Args:
            path (str): The requested path
            excluded_paths (List[str]): List of paths to exclude from authentication

        Returns:
            bool: False (default behavior)
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns None for now, to be implemented later

        Args:
            request (flask.Request, optional): The Flask request object

        Returns:
            None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None for now, to be implemented later

        Args:
            request (flask.Request, optional): The Flask request object

        Returns:
            None
        """
        return None
