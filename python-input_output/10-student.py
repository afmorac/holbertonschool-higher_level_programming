#!/usr/bin/python3
"""
Clase Student que convierte a JSON sus atributos
opcion de filtracion anadida
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


def to_json(self, attrs=None):
    """
    Devuelve diccionario de atributos con filtro
    """
    if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
    else:
        return self.__dict__
