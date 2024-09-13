#!/usr/bin/env python3
"""
Obfuscate log message
"""
import re


def filter_datum(fields, redaction, message, separator) -> str:
    """
    Obfuscate log message
    """
    for field in fields:
        message = re.sub('(?<=' + field + '=)[^;]+', redaction, message)
    return message
