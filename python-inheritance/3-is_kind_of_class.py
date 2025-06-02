#!/usr/bin/python3
"""
Funcion q verifica si un objeto es instancia directa o indirecta
(es decir, si hereda o no) de una clase dada.
"""


def is_kind_of_class(obj, a_class):
    """
    Devuelve True si obj es instancia o hereda de a_class.

    Args:
        obj: el objeto q vamos a verificar
        a_class: la clase base

    Returns:
        True si obj es instancia directa o por herencia de a_class
    """
    return isinstance(obj, a_class)
