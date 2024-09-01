#!/usr/bin/env python3
"""Module task 5"""
import bcrypt


def hash_password(password: str) -> bytes:
    """This fucntion retunns a hashed password"""
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """This fucntion checks if the password is valid or not"""
    return bcrypt.checkpw(password.encode(), hashed_password)
