#!/usr/bin/python3
"""Este módulo define un cuadrado que ya se puede modificar desde fuera,
pero de forma controlada gracias al getter y setter.
"""


class Square:
    """Representa un cuadrado. Permite acceder y cambiar el tamaño,
    pero solo si es un entero positivo.
    """
    def __init__(self, size=0):
        """Inicializa el cuadrado.
        Verifica que el tamaño sea entero y no negativo.
        """
        self.size = size

    @property
    def size(self):
        """Devuelve el tamaño actual del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Permite cambiar el tamaño del cuadrado.
        Solo acepta enteros mayores o iguales que 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Devuelve el área del cuadrado (size al cuadrado)."""
        return self.__size ** 2
