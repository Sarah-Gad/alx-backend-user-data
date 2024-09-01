#!/usr/bin/env python3
"""Module task 5"""
import bcrypt


def hash_password(password: str) -> bytes:
    """This fucntion retunns a hashed password"""
    hashed = bcrypt.hashpw(b'password', bcrypt.gensalt())
    return hashed
