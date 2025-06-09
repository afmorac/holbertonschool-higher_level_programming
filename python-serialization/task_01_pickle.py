#!/usr/bin/env python3
"""Pickling Custom Classes"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializa la instancia y la guarda en un archivo"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            pass  # No lanza error, simplemente ignora si falla

    @classmethod
    def deserialize(cls, filename):
        """Deserializa una instancia desde un archivo"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
