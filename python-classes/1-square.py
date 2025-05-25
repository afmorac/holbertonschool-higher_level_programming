#!/usr/bin/python3
"""Este módulo define una clase que representa un cuadrado con un tamaño.
Ahora mismo no se valida ese tamaño, solo se guarda de manera privada.
"""


class Square:
    """Clase que representa un cuadrado. Se guarda el tamaño de forma privada
    pa' que después podamos controlar mejor qué valores se permiten.
    """
    def __init__(self, size):
        """Inicializa el cuadrado con un tamaño (size).
        No se verifica si el valor es válido todavía.
        """
        self.__size = size
