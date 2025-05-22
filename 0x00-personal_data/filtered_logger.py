import logging
from typing import List, Tuple

PII_FIELDS: Tuple[str, ...] = ("name", "email", "ssn", "password", "phone")

class RedactingFormatter(logging.Formatter):
    # Your existing code for RedactingFormatter here

def get_logger() -> logging.Logger:
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger
