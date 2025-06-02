#!/usr/bin/python3
"""
Clase base de geometría con método area() y validador de enteros
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
