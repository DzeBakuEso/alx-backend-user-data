#!/usr/bin/env python3
"""DB module for managing database interactions."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """Database helper class."""

    def __init__(self) -> None:
        """Initialize engine and session."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized SQLAlchemy session."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: bytes) -> User:
        """Add a new user and return it."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Find the first user matching kwargs.

        Raises:
            NoResultFound: No matching user.
            InvalidRequestError: Bad query field.
        """
        if not kwargs:
            raise InvalidRequestError
        return self._session.query(User).filter_by(**kwargs).one()

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user attributes if valid, else raise ValueError."""
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)
        self._session.commit()
