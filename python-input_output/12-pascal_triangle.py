#!/usr/bin/python3
"""
Triangulo de Pascal
"""


def pascal_triangle(n):
    """
    retorna lista de integers en forma de triangulo pascal
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, len(prev_row)):
            value = prev_row[j - 1] + prev_row[j]
            new_row.append(value)
        new_row.append(1)
        triangle.append(new_row)
    return triangle
