#!/usr/bin/env python3
"""
Clase VerboseList que extiende list y notifica acciones
"""


class VerboseList(list):
    """
    Lista que avisa cuando se modifica (append, extend, remove, pop)
    """

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        cantidad = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{cantidad}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
