#!/usr/bin/python3
"""
Mod. define la funcion de to_json_string
"""


import json


def to_json_string(my_obj):
    """
    Devuelve la representacion json en string de un obj python
    """
    return json.dumps(my_obj)
