#!/usr/bin/env python3
"""App module for user authentication service"""

from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
auth = Auth()


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """
    Update user's password using reset token.
    Expects form data with 'email', 'reset_token', and 'new_password'.
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    if not email or not reset_token or not new_password:
        abort(400, description="Missing email, reset_token or new_password")

    try:
        auth.update_password(reset_token=reset_token, password=new_password)
    except ValueError:
        abort(403)  # Forbidden if token invalid

    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
