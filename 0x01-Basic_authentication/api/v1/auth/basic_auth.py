#!/usr/bin/env python3
"""This module defines a child class"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """This is a child class that inherit from Auth class"""
    def __init__(self) -> None:
        super().__init__()

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """this method will return the Base64 part"""
        if authorization_header is None:
            return None
        elif not isinstance(authorization_header, str):
            return None
        elif not authorization_header.startswith("Basic "):
            return None
        else:
            first, second = authorization_header.split(" ")
            return second
