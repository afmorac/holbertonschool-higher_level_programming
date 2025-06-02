#!/usr/bin/env python3
"""
Uso de clases abstractas y duck typing con figuras geometricas
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Clase abstracta para figuras con area y perímetro
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Clase círculo que implementa Shape
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Clase rectángulo que implementa Shape
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Imprime el área y el perímetro de cualquier figura (duck typing)
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
