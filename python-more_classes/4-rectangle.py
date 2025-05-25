#!/usr/bin/python3
"""Este módulo define un rectángulo con ancho y alto,
se puede imprimir con '#' y también reconstruir con eval().
"""


class Rectangle:
    """Clase que representa un rectángulo.
    Puede calcular área, perímetro, imprimirse con '#' y recrearse con eval().
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

    def __str__(self):
        """Devuelve el rectángulo dibujado con '#'.
        Si width o height es 0, retorna una cadena vacía.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = []
        for _ in range(self.__height):
            lines.append("#" * self.__width)
        return "\n".join(lines)

    def __repr__(self):
        """Devuelve una representación oficial del rectángulo,
        que se puede usar con eval() para crear uno igual.
        """
        return f"Rectangle({self.__width}, {self.__height})"
