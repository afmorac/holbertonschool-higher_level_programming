#!/usr/bin/python3
"""
Clase Square que hereda de Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Clase cuadrado con validación y area heredada
    """

    def __init__(self, size):
        """
        Inicializa el cuadrado con size privado y validado
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
