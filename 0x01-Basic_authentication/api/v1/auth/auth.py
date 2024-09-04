#!/usr/bin/env python3
"""This module is for authentication"""
from flask import request
from typing import List, TypeVar


class Auth():
    """this is the Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method 1"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'
        for pattern in excluded_paths:
            if fnmatch(path, pattern.rstrip('/') + '*'):
                return False
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
