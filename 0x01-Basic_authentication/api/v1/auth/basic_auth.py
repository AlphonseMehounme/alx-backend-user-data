#!/usr/bin/env python3
"""
Basic Auth Module
"""
from api.v1.auth.auth import Auth
import base64


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
