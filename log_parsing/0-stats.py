#!/usr/bin/python3
import sys

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

file_size_total = 0
line_count = 0


def print_stats():
    """Print the accumulated statistics"""
    print("File size: {}".format(file_size_total))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        if len(parts) < 7:
            continue

        # File size is last part
        try:
            file_size_total += int(parts[-1])
        except (ValueError, IndexError):
            continue

        # Status code is second-to-last part
        status = parts[-2]
        if status in status_codes:
            status_codes[status] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Final print in case of clean EOF
print_stats()
