#!/usr/bin/env python3
"""This module is for authentication"""
from flask import request
from typing import List, TypeVar


class Auth():
    """this is the Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method 1"""
        if path is None:
            return True
        elif excluded_paths is None:
            return True
        else:
            if path in excluded_paths or path + "/" in excluded_paths:
                return False
            else:
                return True

    def authorization_header(self, request=None) -> str:
        """Method 2"""
        if request is None:
            return None
        else:
            return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Method 3"""
        return None
