#! /usr/bin/python3
#-*- encoding: utf-8 -*-
# ------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	09/08/2021 00:55:30
#+ Editado:	10/08/2021 20:24:57
# ------------------------------------------------------

import unittest

import sys
sys.path.append('src')
from carta import Carta
from baralla import Baralla

from excepcions import PosicionInexistente, CartaInexistente, BarallaBaleira

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

    def test_str_baleira(self):
        b = Baralla()
        self.assertEqual(str(b), 'Baralla {}\n-------------------\nBaleira'.format(b.get_nome()))

    def test_str_chea(self):
        b = Baralla()
        c = Carta('1', 'a', 'b')
        b.engadir(c)
        self.assertEqual(str(b), 'Baralla {}\n-------------------\n#{}\n{}'.format(b.get_nome(), 1, str(c)))
    
    def test_hash_baleira(self):
        hashes_cartas = []
        b = Baralla()
        for carta in b.get_cartas():
            hashes_cartas.append(hash(carta))
        self.assertEqual(hash(b), hash((b.get_nome(), b.get_preset(), sum(hashes_cartas))))

    def test_hash_chea(self):
        hashes_cartas = []
        b = Baralla()
        b.set_preset('castela')
        for carta in b.get_cartas():
            hashes_cartas.append(hash(carta))
        self.assertEqual(hash(b), hash((b.get_nome(), b.get_preset(), sum(hashes_cartas))))
    # máxicos #

    def test_eliminar_index(self):
        b = Baralla()
        c1 = Carta('1', 'a', 'b')
        c2 = Carta('2', 'a', 'b')
        b.engadir(c1)
        b.engadir(c2)
        b.eliminar_index(0)
        self.assertEqual(1, len(b))
        self.assertEqual(c2, b.get_carta(0))

    def test_eliminar_valor(self):
        b = Baralla()
        c1 = Carta('1', nome='c1', pao='b')
        c2 = Carta('2', nome='c2', pao='b')
        c3 = Carta('2', nome='c3', pao='b')
        c4 = Carta('3', nome='c4', pao='b')
        c5 = Carta('2', nome='c5', pao='b')
        c6 = Carta('4', nome='c6', pao='b')
        b.set_cartas([c1, c2, c3, c4, c5, c6], True)
        b.eliminar_valor('2')
        self.assertEqual(len(b), 3)
        self.assertEqual(b.get_cartas(), [c1,c4,c6])
        self.assertEqual(b.get_carta(0), c1)

    def test_eliminar_pao(self):
        b = Baralla()
        c1 = Carta('1', nome='c1', pao='b')
        c2 = Carta('2', nome='c2', pao='a')
        c3 = Carta('2', nome='c3', pao='a')
        c4 = Carta('3', nome='c4', pao='b')
        c5 = Carta('2', nome='c5', pao='a')
        c6 = Carta('4', nome='c6', pao='b')
        b.set_cartas([c1, c2, c3, c4, c5, c6], True)
        b.eliminar_pao('a'.capitalize())
        self.assertEqual(len(b), 3)
        self.assertEqual(b.get_cartas(), [c1,c4,c6])
        self.assertEqual(b.get_carta(0), c1)

    def test_eliminar_nome(self):
        b = Baralla()
        c1 = Carta('1', nome='c1', pao='b')
        c2 = Carta('2', nome='c', pao='a')
        c3 = Carta('2', nome='c', pao='a')
        c4 = Carta('3', nome='c4', pao='b')
        c5 = Carta('2', nome='c', pao='a')
        c6 = Carta('4', nome='c6', pao='b')
        b.set_cartas([c1, c2, c3, c4, c5, c6], True)
        b.eliminar_nome('c'.capitalize())
        self.assertEqual(len(b), 3)
        self.assertEqual(b.get_cartas(), [c1,c4,c6])
        self.assertEqual(b.get_carta(0), c1)

    def test_eliminar_simbolo(self):
        b = Baralla()
        c1 = Carta('1', nome='c1', pao='b', simbolo='*')
        c2 = Carta('2', nome='c', pao='a', simbolo='+')
        c3 = Carta('2', nome='c', pao='a', simbolo='+')
        c4 = Carta('3', nome='c4', pao='b', simbolo='*')
        c5 = Carta('2', nome='c', pao='a', simbolo='+')
        c6 = Carta('4', nome='c6', pao='b', simbolo='*')
        b.set_cartas([c1, c2, c3, c4, c5, c6], True)
        b.eliminar_simbolo('+')
        self.assertEqual(len(b), 3)
        self.assertEqual(b.get_cartas(), [c1,c4,c6])

    def test_barallar(self):
        b1 = Baralla(preset='poker')
        b2 = Baralla(preset='poker')

        b1.barallar()
        self.assertNotEqual(b1, b2)

    def test_sacar_carta_aleatoria_ok(self):
        b = Baralla()
        c1 = Carta('1', 'a', 'b')
        c2 = Carta('2', 'a', 'b')
        b.engadir(c1)
        b.engadir(c2)
        self.assertEqual(b.sacar_carta(True), c1)
        self.assertEqual(len(b), 1)
        self.assertEqual(b.sacar_carta(True), c2)
        self.assertEqual(len(b), 0)

    def test_sacar_carta_aleatoria_ok(self):
        b = Baralla()
        c = Carta('1', 'a', 'b')
        b.engadir(c)
        self.assertEqual(b.sacar_carta(True), c)
        self.assertEqual(len(b), 0)

    def test_sacar_carta_erro(self):
        b = Baralla()
        self.assertRaises(BarallaBaleira, b.sacar_carta, False)

    def test_sacar_carta_aleatoria_erro(self):
        b = Baralla()
        self.assertRaises(BarallaBaleira, b.sacar_carta, True)

if __name__ == '__main__':
    # para que corran os tests
    unittest.main()

# ------------------------------------------------------
