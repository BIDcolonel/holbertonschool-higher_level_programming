#!/usr/bin/python3
"""Module containing the function pascal_triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s,
    triangle of n.

    Args:
        n (int): rows of triangle.

    Returns:
        list: lists of lists of integers.
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = []
    for index1 in range(n):
        if index1 == 0:
            triangle.append([1])
        else:
            row = [1]
            for index2 in range(1, index1):
                prev_row = triangle[index1 - 1]
                value = prev_row[index2 - 1] + prev_row[index2]
                row.append(value)
            row.append(1)
            triangle.append(row)

    return triangle
