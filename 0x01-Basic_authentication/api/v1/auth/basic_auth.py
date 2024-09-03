#!/usr/bin/env python3
"""This module defines a child class"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """This is a child class that inherit from Auth class"""
    def __init__(self) -> None:
        super().__init__()
