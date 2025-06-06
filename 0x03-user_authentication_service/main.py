#!/usr/bin/env python3
"""
Main module for end-to-end integration test.
"""
import requests

BASE_URL = "http://localhost:5000"

def register_user(email: str, password: str) -> None:
    response = requests.post(f"{BASE_URL}/users", data={'email': email, 'password': password})
    print("register_user:", response.status_code, response.text)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}

def log_in_wrong_password(email: str, password: str) -> None:
    response = requests.post(f"{BASE_URL}/sessions", data={'email': email, 'password': password})
    print("log_in_wrong_password:", response.status_code, response.text)
    assert response.status_code == 401

def log_in(email: str, password: str) -> str:
    response = requests.post(f"{BASE_URL}/sessions", data={'email': email, 'password': password})
    print("log_in:", response.status_code, response.text)
    assert response.status_code == 200
    session_id = response.cookies.get('session_id')
    assert session_id is not None
    return session_id

def profile_unlogged() -> None:
    response = requests.get(f"{BASE_URL}/profile")
    print("profile_unlogged:", response.status_code, response.text)
    assert response.status_code == 403

def profile_logged(session_id: str) -> None:
    cookies = {'session_id': session_id}
    response = requests.get(f"{BASE_URL}/profile", cookies=cookies)
    print("profile_logged:", response.status_code, response.text)
    assert response.status_code == 200

def log_out(session_id: str) -> None:
    cookies = {'session_id': session_id}
    response = requests.delete(f"{BASE_URL}/sessions", cookies=cookies)
    print("log_out:", response.status_code, response.text)
    assert response.status_code == 200

def reset_password_token(email: str) -> str:
    response = requests.post(f"{BASE_URL}/reset_password", data={'email': email})
    print("reset_password_token:", response.status_code, response.text)
    assert response.status_code == 200
    reset_token = response.json().get('reset_token')
    assert reset_token is not None
    return reset_token

def update_password(email: str, reset_token: str, new_password: str) -> None:
    data = {'email': email, 'reset_token': reset_token, 'new_password': new_password}
    response = requests.put(f"{BASE_URL}/reset_password", data=data)
    print("update_password:", response.status_code, response.text)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
