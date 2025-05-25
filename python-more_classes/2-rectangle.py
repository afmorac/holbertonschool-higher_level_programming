#!/usr/bin/python3
"""Este módulo define un rectángulo real con ancho y alto,
y ahora también calcula el área y el perímetro.
"""


class Rectangle:
    """Clase que representa un rectángulo.
    Tiene validaciones y ahora puede calcular su área y perímetro.
    """
    def __init__(self, width=0, height=0):
        """Inicializa el rectángulo con ancho y alto opcionales."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Devuelve el ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Valida y asigna el ancho del rectángulo."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Devuelve el alto del rectángulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Valida y asigna el alto del rectángulo."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Devuelve el área del rectángulo (ancho * alto)."""
        return self.__width * self.__height

    def perimeter(self):
        """Devuelve el perímetro del rectángulo.
        Si alguno de los lados es 0, el perímetro es 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
