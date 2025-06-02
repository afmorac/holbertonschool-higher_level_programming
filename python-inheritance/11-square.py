#!/usr/bin/python3
"""
Clase Square que hereda de Rectangle y redefine __str__
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Clase cuadrado con su propia representacion string
    """

    def __init__(self, size):
        """
        Inicializa el cuadrado con size validado y privado
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Devuelve string como [Square] <size>/<size>
        """
        return f"[Square] {self.__size}/{self.__size}"
