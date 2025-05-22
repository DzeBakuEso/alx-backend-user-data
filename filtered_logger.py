#!/usr/bin/env python3
"""
Module for filtering personal data from log messages.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    pattern = r'({}=)[^{}]*'.format('|'.join(fields), separator)
    return re.sub(pattern, r'\1{}'.format(redaction), message)
