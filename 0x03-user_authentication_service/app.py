#!/usr/bin/env python3
"""This module sets up a flask app"""
from flask import Flask, jsonify, make_response, abort
from flask import redirect, url_for
from auth import Auth
from flask import request
from sqlalchemy.orm.exc import NoResultFound


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
        response = make_response(
            jsonify(
                {"email": email, "message": "logged in"}))
        response.set_cookie(
            key="session_id",
            value=session_id
        )
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """This method is used for logging out"""
    cookies = request.cookies
    session_id = cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect(url_for('homepage'))


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """Profile method"""
    cookies = request.cookies
    session_id = cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """This method is for resetting password"""
    email = request.form.get("email")
    try:
        user = AUTH._db.find_user_by(email=email)
    except NoResultFound:
        abort(403)
    reset_token = AUTH.get_reset_password_token(user.email)
    return jsonify({"email": user.email, "reset_token": reset_token}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
