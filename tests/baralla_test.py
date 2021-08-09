#! /usr/bin/python3
#-*- encoding: utf-8 -*-
# ------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	09/08/2021 00:55:30
#+ Editado:	09/08/2021 19:43:11
# ------------------------------------------------------

import unittest

import sys
sys.path.append('src')
from carta import Carta
from baralla import Baralla

class TestBaralla(unittest.TestCase):

    # getters
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

    def test_get_carta_erro(self):
        b = Baralla()
        self.assertRaises(Exception, b.get_carta, 1)

    def test_get_carta(self):
        b = Baralla()
        carta = Carta('', '', '')
        b.engadir(carta)
        carta2 = b.get_carta(0)
        self.assertEqual(carta, carta2)
    # getters #

    # setters
    def test_set_nome(self):
        nome = 'nome'
        novo_nome = 'novo_nome'
        b = Baralla(nome=nome)
        self.assertEqual(b.get_nome(), nome)
        b.set_nome(novo_nome)
        self.assertEqual(b.get_nome(), novo_nome)

    def test_set_preset(self):
        preset = 'joker'
        novo_preset = 'castela'
        b = Baralla(preset=preset)
        self.assertEqual(b.get_preset(), preset)
        b.set_preset(novo_preset)
        self.assertEqual(b.get_preset(), novo_preset)

    def test_set_cartas(self):
        b = Baralla()
        c1 = Carta('1', '', '')
        c2 = Carta('2', '', '')
        b.set_cartas([c1, c2])
        self.assertEqual(b.get_cartas(), [c1, c2])

    # setters #

    # máxicos
    def test_len(self):
        b = Baralla()
        b.set_preset('poker')
        self.assertEqual(len(b), 50)

    # máxicos #

if __name__ == '__main__':
    # para que corran os tests
    unittest.main()

# ------------------------------------------------------
