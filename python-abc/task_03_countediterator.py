#!/usr/bin/env python3
"""
Clase CountedIterator que extiende un iterador y lleva cuenta
"""


class CountedIterator:
    """
    Iterador que cuenta cuántos elementos se han iterado
    """

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)  # Esto lanza StopIteration si ya no hay
        self.count += 1
        return item

    def get_count(self):
        return self.count

    def __iter__(self):
        return self
