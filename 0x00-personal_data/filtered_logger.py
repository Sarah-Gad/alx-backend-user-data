#!/usr/bin/env python3
"""This module defines the filter_datum fucntion"""
import logging
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        msg = super(RedactingFormatter, self).format(record)
        r_m = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return r_m
