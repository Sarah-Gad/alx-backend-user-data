#!/usr/bin/env python3
"""This module is for authentication"""
from flask import request
from typing import List, TypeVar
import re


class Auth():
    """this is the Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method 1"""
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
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
