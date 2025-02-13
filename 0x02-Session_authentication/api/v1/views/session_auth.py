#!/usr/bin/env python3
"""
Module of Session Auth views
"""
from api.v1.views import app_views
from os import getenv
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth_login():
    """
    Handle session auth login
    POST api/v1/auth_session/login
    """
    email = request.form.get('email')
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})
    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            print(session_id)
            response = jsonify(user.to_json())
            response.set_cookie(getenv('SESSION_NAME'), session_id)
            return response
    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def session_auth_logout():
    """
    Session auth logout
    """
    from api.v1.app import auth
    destroy = auth.destroy_session(request)
    if not destroy:
        abort(404)
    return jsonify({}), 200
