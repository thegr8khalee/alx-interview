#!/usr/bin/python3
"""alx-interview"""

import re
import signal
import sys


def print_statistics(total_size, status_code):
    """Prints the total file size and status codes."""
    print("File size: {}".format(total_size))
    for key in sorted(status_code.keys()):
        if status_code[key] > 0:
            print("{}: {}".format(key, status_code[key]))


def status():
    """Log parsing function."""
    total_size = 0
    status_code = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    line_count = 0

    # Signal handler for CTRL + C
    def signal_handler(sig, frame):
        print_statistics(total_size, status_code)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    # Read from stdin
    try:
        for x in sys.stdin:
            pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
            match = re.match(pattern, x)

            if match:
                status_c = match.group(3)
                file_size = int(match.group(4))
                total_size += file_size

                if status_c in status_code:
                    status_code[status_c] += 1

                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_code)

        # Print final stats if the loop ends
        print_statistics(total_size, status_code)

    except KeyboardInterrupt:
        print_statistics(total_size, status_code)
        sys.exit(0)


if __name__ == "__main__":
    status()
