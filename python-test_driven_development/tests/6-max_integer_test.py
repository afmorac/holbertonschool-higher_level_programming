#!/usr/bin/python3
"""Unittest para la función max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_orden_normal(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_orden_diferente(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_numero_grande_al_principio(self):
        self.assertEqual(max_integer([100, 3, 2, 1]), 100)

    def test_numero_negativo(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_lista_con_un_elemento(self):
        self.assertEqual(max_integer([42]), 42)

    def test_lista_vacia(self):
        self.assertEqual(max_integer([]), None)

    def test_todos_iguales(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_valores_mixtos(self):
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_string(self):
        self.assertEqual(max_integer("hola"), 'o')  # porque compara letras como si fueran valores

    def test_lista_de_strings(self):
        self.assertEqual(max_integer(["a", "z", "m"]), "z")
