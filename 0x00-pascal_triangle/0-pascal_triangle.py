#!/usr/bin/python3
"""leetcode"""


def pascal_triangle(n):
    """Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    """
    if n <= 0:
        return []
    
    first_row = [[1]]

    for i in range(n - 1):
        temp = [0] + first_row[-1] + [0]
        row = []
        for j in range(len(first_row[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        first_row.append(row)
    return first_row
