#!/usr/bin/env python3
"""
filtered_logger.py
Securely connects to a MySQL database to read user data
and logs user info with PII redacted.
"""

import os
import logging
import mysql.connector
from typing import List, Tuple


PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """
    Formatter that redacts specified fields in log messages by replacing their values with '***'.
    """

    REDACTION = "***"
    SEPARATOR = "; "

    def __init__(self, fields: Tuple[str, ...], fmt: str = None):
        super().__init__(fmt)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original = super().format(record)
        return self._filter_datum(original)

    def _filter_datum(self, message: str) -> str:
        """
        Replace field values of PII_FIELDS with redaction string.
        Expected message format: 'field1=value1; field2=value2; ...'
        """
        for field in self.fields:
            # Pattern: field=value; replace value with ***
            message = self._redact_field(message, field)
        return message

    def _redact_field(self, message: str, field: str) -> str:
        import re
        pattern = fr"({field}=)([^;]+)"
        return re.sub(pattern, fr"\1{self.REDACTION}", message)


def get_logger() -> logging.Logger:
    """
    Creates and returns a logger named 'user_data' with RedactingFormatter.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    fmt = "[HOLBERTON] %(name)s %(levelname)s %(asctime)s: %(message)s"
    formatter = RedactingFormatter(fields=PII_FIELDS, fmt=fmt)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Returns a MySQLConnection object connected to the secure database
    using credentials from environment variables.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    if not database:
        raise Exception("PERSONAL_DATA_DB_NAME environment variable not set")

    conn = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )
    return conn


def main() -> None:
    """
    Connects to the database, fetches all users,
    and logs their data with PII fields redacted.
    """
    logger = get_logger()
    db = get_db()
    cursor = db.cursor(dictionary=True)  # dict cursor for column access by name

    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()

    for row in rows:
        # Format the log message with all fields key=value separated by "; "
        # PII fields will be redacted by the formatter.
        log_msg = "; ".join(f"{key}={value}" for key, value in row.items()) + ";"
        logger.info(log_msg)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
