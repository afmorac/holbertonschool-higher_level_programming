#!/usr/bin/python3
"""Este módulo define un rectángulo que se puede imprimir
con diferentes símbolos y lleva la cuenta de sus instancias.
"""


class Rectangle:
    """Clase que representa un rectángulo.
    Se puede imprimir con distintos símbolos, recrear con eval()
    y se despide al eliminarse.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Inicializa el rectángulo con ancho y alto opcionales."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Devuelve el rectángulo en forma de string usando print_symbol.
        Si width o height es 0, retorna una cadena vacía.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join(symbol * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Devuelve una representación oficial que se puede usar con eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Mensaje al eliminar la instancia y se reduce el contador."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
