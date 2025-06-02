#!/usr/bin/python3
"""
Funcion q devuelve True si el objeto es instancia de una subclase
de la clase dada, pero no si es exactamente esa clase.
"""


def inherits_from(obj, a_class):
    """
    Verifica si obj hereda (directa o indirectamente) de a_class,
    sin ser exactamente esa clase.

    Args:
        obj: objeto a revisar
        a_class: clase q se supone sea la base

    Returns:
        True si obj es instancia de subclase de a_class, si no, False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
