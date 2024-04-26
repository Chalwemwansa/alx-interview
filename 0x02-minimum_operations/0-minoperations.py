#!/usr/bin/python3
"""module contains a function min_operations that calculates
    the least number of operations to take to reach a given number"""


def minOperations(n):
    """function gets one argument, the number to find the least number
        steps to reach
        i.e given 9 we might have:
            1, 2, 3, 6, 9:
        copy paste, paste, copy paste, paste
        giving 6 minimum operations to copy paste a number"""
    min_operations = 0  # number of operations to take
    current_value = 0
    step = 1  # step in incrementing the current_value
    while (current_value < n):
        # check if current value divides n and is not 0 or 1
        if not (current_value in [0, 1]) and (n % current_value == 0):
            # change the step to the number, copying in our case
            step = current_value
            min_operations += 1  # add one as this is a copy operation
        current_value += step  # our paste operation
        min_operations += 1  # adding one as the above was a paste opertaion
    return min_operations
