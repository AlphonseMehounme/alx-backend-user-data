#!/usr/bin/env python3
"""
Auth Module
"""
import re
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
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] is not '/':
            path = path + '/'
        """if path not in excluded_paths:
            return True"""
        for pat in excluded_paths:
            if re.search(pat, path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Return request autorization header
        """
        if request is None:
            return None
        if 'Authorization' not in list(request.headers.keys()):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar(User):
        """
        Return current user
        """
        return None
