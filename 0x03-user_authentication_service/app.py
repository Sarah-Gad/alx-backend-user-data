#!/usr/bin/env python3
"""This module sets up a flask app"""
from flask import Flask, jsonify, make_response, abort
from auth import Auth
from flask import request


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=["GET"], strict_slashes=False)
def homepage():
    """This is the hoem page"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=["POST"], strict_slashes=False)
def users():
    """This method will register a user"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=["POST"], strict_slashes=False)
def login():
    """This method is for logging in"""
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response(jsonify({"email": email, "message": "logged in"}))
        response.set_cookie(
            key="session_id",
            value=session_id
        )
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
