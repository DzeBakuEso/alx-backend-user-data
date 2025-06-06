#!/usr/bin/env python3
""" Session Authentication views
"""
from flask import request, jsonify, abort
from api.v1.views import app_views
from models.user import User
from os import getenv

# Import the auth instance from api.v1.app
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth_login():
    """POST /auth_session/login route for session authentication"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    session_name = getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)
    return response


@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def session_auth_logout():
    """DELETE /auth_session/logout route to log out and destroy session"""
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
