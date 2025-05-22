#!/usr/bin/python3
"""
Imprime un cuadrado hecho con el carácter #
El tamaño lo decide el número que se le pasa.
"""

def print_square(size):
    """
    Recibe un número entero (size) e imprime un cuadrado de '#' de ese tamaño.

    Si el valor no es válido, lanza un error con el mensaje correcto.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
