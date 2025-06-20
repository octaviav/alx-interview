#!/usr/bin/python3
"""
Module with island_perimeter function
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid: List of lists of integers where 0 = water, 1 = land

    Returns:
        Integer representing perimeter of island
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all 4 directions: up, down, left, right
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if (ni < 0 or ni >= rows or
                        nj < 0 or nj >= cols or
                            grid[ni][nj] == 0):
                        perimeter += 1

    return perimeter
