#!/usr/bin/env python3
"""This module creates a new view to log in"""
from flask import request, jsonify, make_response, abort
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def post_credentials():
    """This method gets the credentials from the form"""
    user_email = request.form.get("email")
    user_password = request.form.get("password")
    if user_email is None:
        return jsonify({"error": "email missing"}), 400
    if user_password is None:
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": user_email})
    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    user = users[0]
    if not user.is_valid_password(user_password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    cookie_name = os.environ.get('SESSION_NAME')
    response = make_response(user.to_json())
    response.set_cookie(
        key=cookie_name,
        value=session_id
    )
    return response


@app_views.route(
        '/auth_session/logout',
        methods=['DELETE'],
        strict_slashes=False)
def logout():
    """This fucntion is for logging out"""
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    else:
        return jsonify({}), 200
