#!/usr/bin/python3
"""
Mod. que define la funcion load_from_json_file
"""


import json


def load_from_json_file(filename):
    """
    Crear objeto de un JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
