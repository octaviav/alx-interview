#!/usr/bin/python3
"""
Pascal's Triangle module
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): The number of rows to generate

    Returns:
        list: Empty list if n <=0
    """
    if n <= 0:
        return []

    p_triangle = [[1]]  # First row is always [1]

    for x in range(1, n):
        prev_row = p_triangle[x-1]
        curr_row = [1]

        for y in range(1, x):
            curr_row.append(prev_row[y-1] + prev_row[y])

        curr_row.append(1)

        p_triangle.append(curr_row)

    return p_triangle
