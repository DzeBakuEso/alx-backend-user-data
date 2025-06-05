#!/usr/bin/env python3
"""Flask app for authentication service."""
from flask import Flask, request, jsonify, abort, make_response
from auth import Auth

app = Flask(__name__)
auth = Auth()


@app.route('/sessions', methods=['POST'])
def login():
    """POST /sessions route: logs in a user."""
    email = request.form.get('email')
    password = request.form.get('password')

    if not auth.valid_login(email, password):
        abort(401)

    session_id = auth.create_session(email)
    if not session_id:
        abort(401)

    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response
