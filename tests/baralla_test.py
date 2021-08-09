#! /usr/bin/python3
#-*- encoding: utf-8 -*-
# ------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	09/08/2021 00:55:30
#+ Editado:	09/08/2021 14:29:48
# ------------------------------------------------------

import unittest

import sys
sys.path.append('src')
from baralla import Baralla

class TestBaralla(unittest.TestCase):

    def test_get_nome(self):
        nome = 'nome'
        b = Baralla(nome=nome)
        self.assertEqual(b.get_nome(), nome)
    
    def test_get_preset(self):
        preset = 'poker'
        b = Baralla(preset=preset)
        self.assertEqual(b.get_preset(), preset)

    def test_get_cartas(self):
        b = Baralla()
        self.assertEqual(b.get_cartas(), [])

# para que corran os tests
unittest.main()

# ------------------------------------------------------
