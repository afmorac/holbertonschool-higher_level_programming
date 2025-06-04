#!/usr/bin/python3
"""
Mod. que define append_write
"""


def append_write(filename="", text=""):
    """
    Anade txt al final del archivo y retorna caracteres
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
