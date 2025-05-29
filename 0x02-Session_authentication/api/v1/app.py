#!/usr/bin/env python3
"""
App initialization module for API v1.
Initializes Flask app and auth system based on environment variables.
"""

import os
from flask import Flask, jsonify, request

auth = None

auth_type = os.getenv("AUTH_TYPE")

if auth_type == "session_exp_auth":
    from api.v1.auth.session_exp_auth import SessionExpAuth
    auth = SessionExpAuth()
elif auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """
    Simple welcome endpoint.
    """
    return jsonify({"message": "Welcome to the API"}), 200


@app.route('/api/v1/users/me', methods=['GET'])
def get_current_user():
    """
    Example endpoint to get current user info.
    This requires session-based authentication.
    """
    session_id = request.cookies.get(os.getenv("SESSION_NAME", "_my_session_id"))
    if session_id is None:
        return jsonify({"error": "Forbidden"}), 403

    user_id = auth.user_id_for_session_id(session_id)
    if user_id is None:
        return jsonify({"error": "Forbidden"}), 403

    # For demo: Return user_id, in real app fetch user data from DB
    return jsonify({"user_id": user_id}), 200


if __name__ == '__main__':
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 5000))
    app.run(host=host, port=port)
