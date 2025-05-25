#!/usr/bin/python3
"""Este módulo define un cuadrado con validación de tamaño
y también permite calcular su área.
"""


class Square:
    """Representa un cuadrado. Ahora chequea que el tamaño
    sea un número entero y que no sea negativo.
    """
    def __init__(self, size=0):
        """Inicializa el cuadrado. Si el size no es un entero
        o es menor que 0, se lanza un error.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Devuelve el área del cuadrado (size * size)."""
        return self.__size ** 2
