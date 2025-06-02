#!/usr/bin/python3
"""
Este modulo tiene una funcion q te deja ver todo lo q tiene un objeto
por dentro, como sus metodos y atributos disponibles.
"""


def lookup(obj):
    """
    Devuelve una lista de atributos y metodos disponibles pa un objeto.

    Args:
        obj: El objeto q vamos a mirar por dentro

    Returns:
        list: Una lista (tipo lista normal) con todos los nombres
        de metodos y cosas q tiene
    """
    # usa dir, q es como un scanner pa ver lo q hay dentro del obj
    return dir(obj)
