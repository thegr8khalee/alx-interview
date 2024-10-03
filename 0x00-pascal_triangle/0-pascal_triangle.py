#!/usr/bin/python3
"""leetcode
"""


def pascal_triangle(n):
    """_summary_

    Args:
        n (_type_): _description_
    """
    first_row = [[1]]

    for i in range(n - 1):
        temp = [0] + first_row[-1] + [0]
        row = []
        for j in range(len(first_row[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        first_row.append(row)
    return first_row
