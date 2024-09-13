#!/usr/bin/env python3
"""
Main file
"""
import requests

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(EMAIL, PASSWD):
    resonse = requests.post(
        "http://localhost:5000/users",
        data={"email": EMAIL, "password": PASSWD})
    assert resonse.status_code == 200
    assert resonse.json() == {"email": EMAIL, "message": "user created"}


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
