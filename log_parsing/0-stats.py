#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics:
- Total file size
- Count of status codes
It prints stats every 10 lines or when interrupted by CTRL+C.
"""

import sys
import re
from collections import defaultdict

# Track total file size and status code counts
total_size = 0
status_codes = defaultdict(int)
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0


def print_stats():
    """Prints the statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        match = re.search(
            r'(?P<ip>\S+) - \[.*?\] "GET /projects/260 HTTP/1.1" '
            r'(?P<code>\d{3}) (?P<size>\d+)', line)
        if match:
            status = match.group('code')
            size = int(match.group('size'))
            total_size += size
            if status in valid_codes:
                status_codes[status] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
