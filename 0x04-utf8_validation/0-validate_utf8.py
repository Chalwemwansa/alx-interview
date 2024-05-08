#!/usr/bin/python3
"""checks if a given sequence contains valid utf8 data"""


def validUTF8(data):
    """function checks if a given byte in the list is a valid unicode
    character"""
    remaining_bytes = 0

    for num in data:
        if remaining_bytes == 0:
            mask = 0x80
            while mask & num:
                remaining_bytes += 1
                mask >>= 1

            if remaining_bytes == 0:
                continue

            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

        else:
            if not (num & 0b10000000 and not num & 0b01000000):
                return False

        remaining_bytes -= 1

    return remaining_bytes == 0
