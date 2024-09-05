#!/usr/bin/env python3
"""This module defines a child class"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """This class is for the session authentication"""
    def __init__(self) -> None:
        super().__init__()
