#!/usr/bin/env python3
"""This module defines a child class"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """This method returns the decoded str"""
        if base64_authorization_header is None:
            return None
        elif not isinstance(base64_authorization_header, str):
            return None
        else:
            try:
                return base64.b64decode(
                    base64_authorization_header.encode(
                        "utf_8")).decode("utf_8")
            except(base64.binascii.Error, ValueError):
                return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """This method returns the credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        elif not isinstance(decoded_base64_authorization_header, str):
            return None, None
        elif ":" not in decoded_base64_authorization_header:
            return None, None
        else:
            email, password = decoded_base64_authorization_header.split(":")
            return email, password
