#!/usr/bin/env python3
import re

def filter_datum(fields, redaction, message, separator):
        pattern = separator.join(f'({field})' for field in fields)
            return re.sub(pattern, lambda match: separator.join(redaction if group else '' for group in match.groups()), message)
