#!/usr/bin/python3
"""_summary_"""


def rotate_2d_matrix(matrix):
    """_summary_

    Args:
        matrix (_type_): _description_
    """
    left, right = 0, len(matrix) - 1

    while right > left:
        for i in range(right - left):
            top, bottom = left, right

            # save top left
            top_left = matrix[top][left + i]

            # move bottom_left to top_left
            matrix[top][left + i] = matrix[bottom - i][left]

            # move bottom_right to bottom_left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # move top_right to bottom_right
            matrix[bottom][right - i] = matrix[top + i][right]

            # move top_left to top_right
            matrix[top + i][right] = top_left
        right -= 1
        left += 1
