#!/usr/bin/python3
"""Este módulo define un rectángulo real, ya con ancho y alto,
y validación pa' que no se metan valores negativos ni raros.
"""


class Rectangle:
    """Clase que representa un rectángulo. Aquí ya usamos
    ancho y alto privados, con validación por si acaso.
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
