#!/usr/bin/python3
"""
Devuelve diccionario con atributos de objeto
para convertirlo a JSON serializable
"""


def class_to_json(obj):
    return obj.__dict__
