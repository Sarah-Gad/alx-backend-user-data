#!/usr/bin/env python3
"""This module defines the filter_datum fucntion"""
import logging
import os
import re
from typing import List
import mysql.connector
from mysql.connector import connection


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """This fucntion cerates a new logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    console_handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """This fucntion returns a connector to the DB"""
    connt = mysql.connector.connect(
        user=os.environ.get("PERSONAL_DATA_DB_USERNAME"),
        password=os.environ.get("PERSONAL_DATA_DB_PASSWORD"),
        host=os.environ.get("PERSONAL_DATA_DB_HOST"),
        database=os.environ.get("PERSONAL_DATA_DB_NAME")
    )
    return connt


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
        """This is a method to format the record"""
        msg = super(RedactingFormatter, self).format(record)
        r_m = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return r_m
