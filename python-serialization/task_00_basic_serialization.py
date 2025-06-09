#!/usr/bin/env python3
"""Basic serialization module"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializa un diccionario y lo guarda en un archivo JSON.
    Si el archivo existe, se sobreescribe.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Carga un archivo JSON y devuelve el diccionario correspondiente.
    """
    with open(filename, 'r') as file:
        return json.load(file)
