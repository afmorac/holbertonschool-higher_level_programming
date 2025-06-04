#!/usr/bin/python3
"""
Mod. define la funcion write_file
"""


def write_file(filename="", text=""):
    """
    Func. escribir cadena a txt file
    retornar numero de caracteres
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
