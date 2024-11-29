#!/usr/bin/env python3
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
        pattern = separator.join(f'({field})' for field in fields)
            return re.sub(pattern, lambda match: separator.join(redaction if group else '' for group in match.groups()), message)
