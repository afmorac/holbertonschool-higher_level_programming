#!/usr/bin/python3
"""Este módulo define un cuadrado, lo puedes modificar, 
sacar el área y también imprimirlo con '#'.
"""

class Square:
    """Representa un cuadrado con tamaño ajustable.
    También se puede imprimir visualmente usando '#'.
    """
    def __init__(self, size=0):
        """Inicializa el cuadrado con un tamaño opcional."""
        self.size = size

    @property
    def size(self):
        """Devuelve el tamaño actual del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Permite cambiar el tamaño, pero con validación."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Devuelve el área del cuadrado (size * size)."""
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado con '#' según su tamaño.
        Si size es 0, solo imprime una línea en blanco.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
