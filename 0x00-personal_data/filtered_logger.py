#!/usr/bin/env python3
"""
Obfuscate log message
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscate log message
    """
    for field in fields:
        message = re.sub('(?<=' + field + '=)[^' + separator + ';]+',
                         redaction, message)
    return message
