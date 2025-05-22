#!/usr/bin/python3
"""
Imprime el texto con dos líneas nuevas después de cada punto, signo de pregunta o dos puntos.
No deja espacios al principio de las líneas nuevas.
"""

def text_indentation(text):
    """
    Recibe un texto y mete dos saltos de línea después de ., ? y :

    Si no le das un string, lanza error.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = True
    for char in text:
        if new_line and char == ' ':
            continue
        else:
            new_line = False

        print(char, end="")

        if char in ".:?":
            print("\n")
            new_line = True
