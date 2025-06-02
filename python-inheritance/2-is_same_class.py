#!/usr/bin/python3
"""
Funcion pa verificar si un objeto es exactamente de una clase,
sin importar si hereda o no. Tiene q ser la misma clase exacta.
"""

def is_same_class(obj, a_class):
    """
    Devuelve True si obj es exactamente una instancia de a_class.

    Args:
        obj: cualquier objeto
        a_class: la clase con la q queremos comparar

    Returns:
        True si obj es exactamente instancia de a_class, si no, False
    """
    return type(obj) is a_class
