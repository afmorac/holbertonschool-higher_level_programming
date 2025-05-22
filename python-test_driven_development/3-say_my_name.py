#!/usr/bin/python3
"""
Imprime: My name is <first name> <last name>
Si no es string, tira error.
"""

def say_my_name(first_name, last_name=""):
    """
    Recibe un nombre y un apellido y lo imprime.

    Si no son strings, lanza error.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
