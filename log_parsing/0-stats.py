#!/usr/bin/python3
import sys


def print_stats(file_size, status_counts):
    """Print the file size and the status code counts."""
    print(f"File size: {file_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


file_size = 0
status_counts = {200: 0, 301: 0, 400: 0,
                 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Check if line is in the expected format
        if len(parts) >= 7:
            try:
                # Extract file size and status code
                file_size += int(parts[-1])
                status_code = int(parts[-2])

                # Update status code count if valid
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except ValueError:
                # If conversion fails, ignore that line
                pass

        # Every 10 lines, print the statistics
        if line_count % 10 == 0:
            print_stats(file_size, status_counts)

except KeyboardInterrupt:
    # On keyboard interrupt, print the current statistics
    print_stats(file_size, status_counts)
    raise

# Print final stats after EOF (end of input)
print_stats(file_size, status_counts)
