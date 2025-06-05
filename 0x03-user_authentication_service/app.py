#!/usr/bin/env python3
"""Flask application providing basic auth routes."""
from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome() -> str:
    """Root route returning a welcome message."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """
    POST /users
    Register a user with form fields: email, password.
    Success   → 200,  {"email": email, "message": "user created"}
    Duplicate → 400,  {"message": "email already registered"}
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None or password is None:
        return jsonify({"message": "email and password required"}), 400

    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": email, "message": "user created"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
