#!/usr/bin/python3
"""
Mod. define la funcion save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Guarda un obj en un archivo usando JSON
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
