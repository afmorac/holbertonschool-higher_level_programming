#!/usr/bin/python3
"""
Clase Rectangle que hereda de BaseGeometry y define area y __str__
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Clase rectángulo con validación y area definida
    """

    def __init__(self, width, height):
        """
        Inicializa con width y height privados y validados
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Devuelve el área del rectángulo
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Devuelve la representación string del rectángulo
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
