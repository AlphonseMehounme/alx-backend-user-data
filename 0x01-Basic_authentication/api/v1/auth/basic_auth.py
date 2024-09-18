#!/usr/bin/env python3
"""
Basic Auth Module
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    BasicAuth Class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extract base64 authorization header
        """
        if authorization_header is None or type(authorization_header) != str:
            return None
        if authorization_header.split()[0] != 'Basic':
            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """
        Decode authorization header
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            encoded = base64_authorization_header.encode('utf-8')
            return base64.b64decode(encoded).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        Extract user credentials
        """
        decoded = decoded_base64_authorization_header
        if decoded is None or type(decoded) != str or ':' not in decoded:
            return (None, None)
        credentials = decoded.split(':')
        return (credentials[0], credentials[1])

    def user_object_from_credentials(self, user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """
        Return user object based on credentials
        """
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        users = User.search({'email': user_email})
        if len(users) == 0:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return current user
        """
        auth_h = self.authorization_header(request)
        if auth_h is None:
            return None
        b64_auth_h = self.extract_base64_authorization_header(auth_h)
        if b64_auth_h is None:
            return None
        decoded_b64_auth = self.decode_base64_authorization_header(b64_auth_h)
        if decoded_b64_auth is None:
            return None
        credentials = self.extract_user_credentials(decoded_b64_auth)
        if credentials is None:
            return None
        user_email = credentials[0]
        user_pwd = credentials[1]
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
