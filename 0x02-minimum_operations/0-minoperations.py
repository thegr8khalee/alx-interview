#!/usr/bin/python3
"""alx-interview"""


def minOperations(n):
    """_summary_

    Args:
        n (_type_): _description_
    """
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1

    return operations
