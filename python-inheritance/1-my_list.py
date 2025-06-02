#!/usr/bin/python3
"""
Clase MyList q hereda de list y tiene un metodo pa imprimir
la lista ordenada sin cambiar el orden original.
"""


class MyList(list):
    """
    Clase q extiende list pa añadir print_sorted
    """

    def print_sorted(self):
        """
        Imprime la lista ordenada (sin modificar la original)
        """
        print(sorted(self))
