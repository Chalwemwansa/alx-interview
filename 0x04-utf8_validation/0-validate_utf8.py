#!/usr/bin/python3
"""this module contains the validUTF8 function"""


def validUTF8(data):
    """function checks if the list passed in contains
    only valid utf8 characters"""
    for integer in data:
        more_than = integer > 1114111
        less_than = integer <= 0
        invalid = (integer & 255) == 0
        if more_than or less_than or invalid:
            return False
    return True
