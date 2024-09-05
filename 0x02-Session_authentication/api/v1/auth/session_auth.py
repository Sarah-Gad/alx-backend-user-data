#!/usr/bin/env python3
"""This module defines a child class"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """This class is for the session authentication"""
    user_id_by_session_id = {}

    def __init__(self) -> None:
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """This method creates  a session id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = uuid.uuid4()
        SessionAuth.user_id_by_session_id[str(session_id)] = user_id
        return session_id
