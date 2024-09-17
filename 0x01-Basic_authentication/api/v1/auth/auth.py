"""
Auth Module
"""
from flask import request
from typing import List, TypeVar
from api.v1.views import User


class Auth:
    """
    Class Auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if a path requires auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Return request autorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar(User):
        """
        Return current user
        """
        return None
