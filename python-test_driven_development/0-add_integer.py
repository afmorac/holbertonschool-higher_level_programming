#!/usr/bin/python3
"""
Función sencilla que suma dos números.
Acepta enteros o floats, pero siempre devuelve un entero.
"""

def add_integer(a, b=98):
    """
    Suma dos números (enteros o flotantes).

    Si alguno no es número, lanza un error.
    Convierte los float a int antes de sumar.

    Args:
        a: primer número
        b: segundo número (por defecto es 98)

    Returns:
        La suma de a y b como entero
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
