#!/usr/bin/python3
"""Este módulo define un cuadrado con validación de tamaño 
y también permite calcular su área.
"""

class Square:
    """Representa un cuadrado con tamaño validado.
    Se puede calcular el área del cuadrado usando el método area().
    """
    def __init__(self, size=0):
        """Inicializa el cuadrado.
        Verifica que el tamaño sea entero y no negativo.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Devuelve el área del cuadrado (size * size)."""
        return self.__size ** 2
