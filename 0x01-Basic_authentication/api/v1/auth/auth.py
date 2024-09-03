#!/usr/bin/env python3
"""This module is for authentication"""
from flask import request
from typing import List, TypeVar


class Auth():
    """this is the Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method 1"""
        return False

    def authorization_header(self, request=None) -> str:
        """Method 2"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method 3"""
        return None
