#!/usr/bin/python3
"""
Mod. define la funcion from_json_string
"""


import json


def from_json_string(my_str):
    """
    convierte string en formato JSON a obj python
    """
    return json.loads(my_str)
