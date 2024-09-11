#!/usr/bin/env python3
"""This module defines a _hash_password method"""
import bcrypt


def _hash_password(password):
    """This method return returns hasdhed password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
