#!/usr/bin/env python3
"""This module defines a _hash_password method"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """This method return returns hasdhed password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """This fucntion returns a string representation of UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """this method will register a new useer"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {user.email} already exists")
        except NoResultFound:
            pass
        hashed = _hash_password(password)
        created_user = self._db.add_user(email, hashed)
        return created_user

    def valid_login(self, email: str, password: str) -> bool:
        """This method validate credentials"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if bcrypt.checkpw(password.encode(), user.hashed_password):
            return True
        else:
            return False

    def create_session(self, email: str) -> str:
        """This method returns the session id as a string"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_uuid = _generate_uuid()
        self._db.update_user(user.id, session_id=session_uuid)
        return user.session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """This method returns the user object"""
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """This method destroys the session by
        setting the session_id attribute to None"""
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """This method generates a reset password token"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        reset_uuid = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_uuid)
        return user.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """This method is for updating the password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        hashed_pw = _hash_password(password)
        self._db.update_user(
            user.id,
            hashed_password=hashed_pw,
            reset_token=None)
