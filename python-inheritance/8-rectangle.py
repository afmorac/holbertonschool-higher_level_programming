#!/usr/bin/python3
"""
Clase Rectangle que hereda de BaseGeometry sin usar import
Incluye también la definicion de BaseGeometry con validación
"""


class BaseGeometry:
    """
    Clase base de geometría
    """

    def area(self):
        """
        Método que debería calcular el área, pero aún no está implementado
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valida que value sea entero positivo
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Clase rectángulo con validación heredada de BaseGeometry
    """

    def __init__(self, width, height):
        """
        Inicializa con width y height privados y validados
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
