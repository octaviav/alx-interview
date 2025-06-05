#!/usr/bin/python3
"""
Rotate 2D Matrix 90 degrees clockwise in-place
"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix: n x n 2D list representing the matrix

    Returns:
        None (modifies matrix in-place)
    """
    n = len(matrix)

    # Process matrix layer by layer from outside to inside
    for layer in range(n // 2):
        # Define boundaries for current layer
        first = layer
        last = n - 1 - layer

        # Rotate elements in current layer
        for x in range(first, last):
            # Calculate offset from first position
            offset = x - first

            top = matrix[first][x]

            matrix[first][x] = matrix[last - offset][first]

            matrix[last - offset][first] = matrix[last][last - offset]

            matrix[last][last - offset] = matrix[x][last]

            matrix[x][last] = top
