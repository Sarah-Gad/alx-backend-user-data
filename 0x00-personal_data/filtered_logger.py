#!/usr/bin/env python3
"""This module defines the filter_datum fucntion"""
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """This fucntion will return the log message obfuscated"""
    returned = message
    for i in fields:
        pattern = rf'{i}=[^{separator}]*'
        returned = re.sub(pattern, rf'{i}={redaction}', returned)
    return returned
