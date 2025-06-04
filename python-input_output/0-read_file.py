#!/usr/bin/python3
"""
Func. que lee e imprime un archivo
"""

def read_file(filename=""):
    """
    Lectura de archivo de texto y lo muestra en stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
