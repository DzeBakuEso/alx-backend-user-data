#!/usr/bin/env python3
"""Flask app for user authentication service"""

from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
auth = Auth()


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """Route to generate reset password token given email in form data"""
    email = request.form.get('email')
    if not email:
        abort(400, description="Missing email")

    try:
        reset_token = auth.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        abort(403)  # Email not registered


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
