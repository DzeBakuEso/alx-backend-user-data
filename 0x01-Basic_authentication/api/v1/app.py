#!/usr/bin/env python3
""" Main application file for the API
"""
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os

from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

# Enable CORS for API routes
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Determine which authentication system to use
auth = None
auth_type = os.getenv("AUTH_TYPE")

if auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.before_request
def before_request_func():
    """Executed before each request to filter by authentication."""
    if auth is None:
        return

    excluded_paths = [
        "/api/v1/status/",
        "/api/v1/unauthorized/",
        "/api/v1/forbidden/"
    ]

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """Handler for 404 errors"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Handler for 401 errors"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Handler for 403 errors"""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
