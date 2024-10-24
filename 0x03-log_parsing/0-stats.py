# #!/usr/bin/python3
# """alx-interview"""

# import re
# import signal
# import sys


# def print_statistics(total_size, status_code):
#     """Prints the total file size and status codes."""
#     print("File size: {}".format(total_size))
#     for key in sorted(status_code.keys()):
#         if status_code[key] > 0:
#             print("{}: {}".format(key, status_code[key]))


# def status():
#     """Log parsing function."""
#     total_size = 0
#     status_code = {
#         "200": 0,
#         "301": 0,
#         "400": 0,
#         "401": 0,
#         "403": 0,
#         "404": 0,
#         "405": 0,
#         "500": 0,
#     }
#     line_count = 0

#     # Signal handler for CTRL + C
#     def signal_handler(sig, frame):
#         print_statistics(total_size, status_code)
#         sys.exit(0)

#     signal.signal(signal.SIGINT, signal_handler)

#     # Read from stdin
#     try:
#         for x in sys.stdin:
#             pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
#             match = re.match(pattern, x)

#             if match:
#                 status_c = match.group(3)
#                 file_size = int(match.group(4))
#                 total_size += file_size

#                 if status_c in status_code:
#                     status_code[status_c] += 1

#                 line_count += 1

#                 if line_count % 10 == 0:
#                     print_statistics(total_size, status_code)

#         # Print final stats if the loop ends
#         print_statistics(total_size, status_code)

#     except KeyboardInterrupt:
#         print_statistics(total_size, status_code)
#         sys.exit(0)


# if __name__ == "__main__":
#     status()


#!/usr/bin/python3

import sys


def print_msg(dict_sc, total_file_size):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
code = 0
counter = 0
dict_sc = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if code in dict_sc.keys():
                    dict_sc[code] += 1

            if counter == 10:
                print_msg(dict_sc, total_file_size)
                counter = 0

finally:
    print_msg(dict_sc, total_file_size)
