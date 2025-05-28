#!/usr/bin/env python3
"""Basic Authentication module
"""
import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Implements Basic Authentication"""

    def extract_user_credentials(self, base64_auth_header: str) -> (str, str):
        """Extracts user email and password from Base64 string"""
        if base64_auth_header is None or not isinstance(base64_auth_header, str):
            return (None, None)
        try:
            decoded = base64.b64decode(base64_auth_header).decode('utf-8')
            if ':' not in decoded:
                return (None, None)
            email, password = decoded.split(':', 1)
            return (email, password)
        except Exception:
            return (None, None)

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Retrieves a User instance based on email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
            if not users:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve current user from request"""
        auth_header = self.authorization_header(request)
        base64_header = self.extract_base64_authorization_header(auth_header)
        email, pwd = self.extract_user_credentials(base64_header)
        return self.user_object_from_credentials(email, pwd)
