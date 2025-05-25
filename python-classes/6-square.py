#!/usr/bin/python3
"""Este módulo define un cuadrado que se puede mover en pantalla
usando coordenadas con espacios (position).
"""


class Square:
    """Representa un cuadrado que se puede imprimir con '#'
    y mover usando una posición (x, y) de espacios y líneas vacías.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el cuadrado con tamaño y posición opcional."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Devuelve el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Valida y asigna el tamaño del cuadrado."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Devuelve la posición actual del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Valida y asigna la posición (x, y) del cuadrado."""
        if (
            type(value) is not tuple or
            len(value) != 2 or
            not all(type(num) is int and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Devuelve el área del cuadrado (size * size)."""
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado con '#' usando tamaño y posición.
        Si size es 0, solo imprime una línea vacía.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
