#!/usr/bin/env python3
"""
Session Expiration Auth Module
"""
from os import getenv
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """
    SessionExpAuth class
    """
    def __init__(self):
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        Create session
        """
        try:
            session_id = super().create_session(user_id)
        except Exception:
            return None
        session_dict = {'user_id': user_id, 'created_at': datetime.now()}
        self.user_id_by_session_id.update({session_id: session_dict})
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        User id with session id
        """
        if session_id is None:
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None
        if self.session_duration <= 0:
            return session_dict['user_id']
        if 'created_at' not in session_dict.keys():
            return None
        created_at = session_dict['created_at']
        if (created_at + timedelta(seconds=self.session_duration) <
           datetime.now()):
            return None
        return session_dict['user_id']
