#!/usr/bin/python3
"""this module contains the validUTF8 function"""


def validUTF8(data):
    """function checks if the list passed in contains
    only valid utf8 characters"""
    for integer in data:
        if (integer & 255) == 0:
            return False
    return True
