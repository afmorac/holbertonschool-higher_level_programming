#!/usr/bin/python3
"""
Divide todos los elementos de una matriz
y devuelve una nueva con los resultados redondeados a 2 decimales.
"""

def matrix_divided(matrix, div):
    """
    Recibe una matriz (lista de listas) y divide cada número entre div.

    - La matriz debe tener solo ints o floats.
    - Todas las filas deben tener el mismo tamaño.
    - div no puede ser cero y tiene que ser número.

    Devuelve una nueva matriz con los valores divididos y redondeados.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(item / div, 2) for item in row] for row in matrix]
