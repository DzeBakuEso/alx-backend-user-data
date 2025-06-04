#!/usr/bin/env python3
"""
User module

This module defines the User model mapped to the 'users' table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    User model for the 'users' table.

    Attributes:
        id (int): Primary key.
        email (str): User email, non-nullable.
        hashed_password (str): Hashed password, non-nullable.
        session_id (str): Session ID, nullable.
        reset_token (str): Reset token, nullable.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
