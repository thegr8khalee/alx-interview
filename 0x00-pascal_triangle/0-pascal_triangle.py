def pascal_triangle(n):
    """_summary_

    Args:
        n (_type_): _description_
    """
    # create first row
    # loop tru n
    # create first row with 0 at beginning and end
    # create the row
    # loop tru first row
    # append index to the row
    # append row to first row
    # return First row

    first_row = [[1]]

    for i in range(n - 1):
        temp = [0] + first_row[-1] + [0]
        row = []
        for j in range(len(first_row[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        first_row.append(row)
    return first_row
