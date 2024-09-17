#!/usr/bin/env python3
"""
Basic Auth Module
"""
from api.v1.auth.auth import Auth


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
