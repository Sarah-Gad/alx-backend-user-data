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
    splited = message.split(separator)
    returned = message
    for i in splited:
        if i.startswith(fields[0]) or i.startswith(fields[1]):
            spli = i.split("=")
            pattern = re.escape(spli[1])
            returned = re.sub(pattern, redaction, returned)
    return returned
