#!/usr/bin/env python3
"""the module contains code that reads from a file or stdin in general
then gets valid lines and logs them for printing later"""
import sys
import re
import signal
from types import FrameType
from typing import Dict, Optional


# global variables
count: int = 0  # checks if 10 lines have been read, reset if CTR-C
total_file_size: int = 0
status_dict: Dict[int, int] = {}  # status and number of lines with status


def match_str(line: str) -> bool:
    """function takes as input a string then it is matched against
    a regex  to verify if its the write type, if it is the write type
    a dictionary is returned with key value pairs of the
    status code and the file size of eachline"""
    global total_file_size
    global status_dict
    file_size = 0

    #  the pattern to match the line passed into stdin against
    pattern = (
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '  # IP address
        r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] '  # Date
        r'"[A-Z]+ .+" '  # Request line
        r'(\d{3}) '  # Status code
        r'(\d+)$'  # File size
    )

    #  match the line using the regex
    is_match = re.search(pattern, line)

    #  if the line is a match then get the different fields from the regex
    #  using the grouping method
    if is_match:
        status_code: int = int(is_match.group(1))
        file_size: int = int(is_match.group(2))
        if status_code in status_dict:
            status_dict[status_code] += 1
        else:
            status_dict[status_code] = 1
        total_file_size += file_size
        return True
    return False


def sig_handler(sig: signal.Signals, frame: Optional[FrameType]) -> None:
    """the function that handles the control-c signal from the keyboard
    after such a signal is received, the stats are printed to std"""
    print_stats()


def print_stats() -> None:
    """function prints the current state of the values in the dictionary
    and the size of the files"""
    global count
    print("File size: {}".format(total_file_size))
    for key, value in dict(sorted(status_dict.items())).items():
        print("{}: {}".format(key, value))
    count = 0


#  handle the control-c signal
signal.signal(signal.SIGINT, sig_handler)


def main():
    """the main method where execution will start from and loops
    through input"""
    global count
    for line in sys.stdin:
        if match_str(line.strip()):
            count += 1
        if count == 10:
            print_stats()


if __name__ == "__main__":
    """run the main method if current module is executed
    and not when imported"""
    main()
