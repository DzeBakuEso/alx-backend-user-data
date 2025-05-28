#!/usr/bin/env python3
""" Basic authentication module """

import base64
from typing import Tuple, TypeVar, Union
from models.user import User
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic authentication implementation """

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> Union[str, None]:
        """Decode a Base64 encoded authorization header."""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode("utf-8")
            return decoded_str
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[Union[str, None], Union[str, None]]:
        """
        Extract email and password from decoded Base64 authorization header,
        allowing password to contain ':' characters.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split only on the first ':'
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """Retrieve User instance given email and password."""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if not users or len(users) == 0:
            return None
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Overloads Auth.current_user to retrieve the User instance
        based on Basic Auth credentials.
        """
        authorization_header = self.authorization_header(request)
        if authorization_header is None:
            return None

        base64_header = self.extract_base64_authorization_header(
            authorization_header
        )
        if base64_header is None:
            return None

        decoded = self.decode_base64_authorization_header(base64_header)
        if decoded is None:
            return None

        email, pwd = self.extract_user_credentials(decoded)
        if email is None or pwd is None:
            return None

        user = self.user_object_from_credentials(email, pwd)
        return user
