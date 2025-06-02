#!/usr/bin/env python3
"""
Abstract class Animal con sus subclases Dog y Cat
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Clase abstracta Animal que requiere implementar el metodo sound
    """

    @abstractmethod
    def sound(self):
        """
        Metodo abstracto que debe devolver el sonido del animal
        """
        pass


class Dog(Animal):
    """
    Subclase Dog que implementa sound
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Subclase Cat que implementa sound
    """

    def sound(self):
        return "Meow"
