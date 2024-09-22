#!/usr/bin/env python3
"""
Session DB Auth module complete
"""
from datetime import datetime, timedelta
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    SessionDBAuth class
    """

    def create_session(self, user_id=None):
        """
        Create new session
        """
        if user_id is None:
            return None
        session_id = super().create_session(user_id)
        usersession = UserSession(user_id=user_id, session_id=session_id)
        usersession.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Search user id by session id
        """
        if session_id is None:
            return None
        usersession = UserSession.search({'session_id': session_id})
        if len(usersession) == 0:
            return None
        if self.session_duration <= 0:
            return usersession[0].user_id
        session_dict = self.user_id_by_session_id.get(session_id)
        if 'created_at' not in session_dict.keys():
            return None
        created_at = session_dict['created_at']
        if (created_at + timedelta(seconds=self.session_duration) <
           datetime.now()):
            return None
        return usersession[0].user_id

    def destroy_session(self, request=None):
        """
        Destroy session
        """
        session_id = self.session_cookie(request)
        usersession = UserSession.search({'session_id': session_id})
        if len(usersession) == 0:
            return False
        usersession[0].remove()
        return True
