#! /usr/bin/python3
#-*- encoding: utf-8 -*-
# ------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	09/08/2021 00:54:34
#+ Editado:	09/08/2021 14:13:03
# ------------------------------------------------------

import unittest

import sys
sys.path.append('src')
from carta import Carta

class TestCarta(unittest.TestCase):

    # constructor
    def test_crear_carta_con_nones(self):
        Carta('','','')
    # constructor #
        
    # getters
    def test_get_valor(self):
        valor = '1'
        c = Carta(valor=valor, pao='Corazóns', nome='Un', simbolo='A')
        self.assertEqual(c.get_valor(), valor)

    def test_get_pao(self):
        pao = 'Corazóns'
        c = Carta(valor='1', pao=pao, nome='Un', simbolo='A')
        self.assertEqual(c.get_pao(), pao)

    def test_get_simbolo(self):
        simbolo='A'
        c = Carta(valor='1', pao='Corazóns', nome='Un', simbolo=simbolo)
        self.assertEqual(c.get_simbolo(), simbolo)

    def test_get_nome(self):
        nome = 'Un'
        c = Carta(valor='1', pao='Corazóns', nome=nome, simbolo='A')
        self.assertEqual(c.get_nome(), nome)
    # getters #

    # setters
    def test_set_valor(self):
        novo= '2'
        velho = '1'
        c = Carta(valor=velho, pao='Corazóns', nome='Un', simbolo='A')
        saida = c.set_valor(novo)
        self.assertTrue(saida)
        self.assertEqual(c.get_valor(), novo)

    def test_set_pao(self):
        novo = 'Picas'
        velho = 'Corazóns'
        c = Carta(valor='1', pao=velho, nome='Un', simbolo='A')
        saida = c.set_pao(novo)
        self.assertTrue(saida)
        self.assertEqual(c.get_pao(), novo)

    def test_set_nome(self):
        novo = 'Nome2'
        velho = 'Nome'
        c = Carta(valor='1', pao='Corazóns', nome=velho, simbolo='A')
        saida = c.set_nome(novo)
        self.assertTrue(saida)
        self.assertEqual(c.get_nome(), novo)

    def test_set_simbolo(self):
        novo = '+'
        velho = '*'
        c = Carta(valor='1', pao='Corazóns', nome='Un', simbolo=velho)
        saida = c.set_simbolo(novo)
        self.assertTrue(saida)
        self.assertEqual(c.get_simbolo(), novo)
    # setters #

    # máxicos
    def test_str_completo(self):
        c = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        self.assertEqual(str(c), 'Símbolo: A\nNome:\t Un\nValor:\t 1\nPao:\t Corazóns')

    def test_str_parte(self):
        c = Carta(valor='1', pao='Corazóns', nome='Un')
        self.assertEqual(str(c), 'Nome:\t Un\nValor:\t 1\nPao:\t Corazóns')

    def test_len(self):
        valor = '1'
        c = Carta(valor=valor, pao='Corazóns', nome='Un', simbolo='A')
        self.assertEqual(len(c), int(valor))

    def test_eq_ok_iguais(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        self.assertTrue(c1 == c2)
    def test_eq_ok_distintos(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='1', pao='Picas', nome='Unn', simbolo='Ah')
        self.assertTrue(c1 == c2)
    def test_eq_erro_iguais(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='2', pao='Corazóns', nome='Un', simbolo='A')
        self.assertFalse(c1 == c2)
    def test_eq_erro_distintos(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='4', pao='Picas', nome='Unn', simbolo='Ah')
        self.assertFalse(c1 == c2)

    def test_ne_erro_iguais(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        self.assertFalse(c1 != c2)
    def test_ne_erro_distintos(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='1', pao='Picas', nome='Unn', simbolo='Ah')
        self.assertFalse(c1 != c2)
    def test_ne_ok_iguais(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='2', pao='Corazóns', nome='Un', simbolo='A')
        self.assertTrue(c1 != c2)
    def test_ne_ok_distintos(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='4', pao='Picas', nome='Unn', simbolo='Ah')
        self.assertTrue(c1 != c2)

    def test_lt_erro_iguais(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        self.assertFalse(c1 < c2)
    def test_lt_erro_distintos(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='1', pao='Picas', nome='Unn', simbolo='Ah')
        self.assertFalse(c1 < c2)
    def test_lt_ok_iguais(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='2', pao='Corazóns', nome='Un', simbolo='A')
        self.assertTrue(c1 < c2)
    def test_lt_ok_distintos(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='4', pao='Picas', nome='Unn', simbolo='Ah')
        self.assertTrue(c1 < c2)

    def test_gt_erro_iguais(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        self.assertFalse(c1 > c2)
    def test_gt_erro_distintos(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='1', pao='Picas', nome='Unn', simbolo='Ah')
        self.assertFalse(c1 > c2)
    def test_gt_ok_iguais(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='2', pao='Corazóns', nome='Un', simbolo='A')
        self.assertTrue(c2 > c1)
    def test_gt_ok_distintos(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='4', pao='Picas', nome='Unn', simbolo='Ah')
        self.assertTrue(c2 > c1)

    def test_le_ok_iguais(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c3 = Carta(valor='0', pao='Corazóns', nome='Un', simbolo='A')
        self.assertTrue(c1 <= c2)
        self.assertTrue(c3 <= c2)
    def test_le_ok_distintos(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='1', pao='Picas', nome='Unn', simbolo='Ah')
        c3 = Carta(valor='0', pao='Corazóns', nome='Un', simbolo='A')
        self.assertTrue(c1 <= c2)
        self.assertTrue(c3 <= c2)
    def test_le_erro_iguais(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='2', pao='Corazóns', nome='Un', simbolo='A')
        self.assertFalse(c2 <= c1)
    def test_le_erro_distintos(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='4', pao='Picas', nome='Unn', simbolo='Ah')
        self.assertFalse(c2 <= c1)

    def test_ge_ok_iguais(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c3 = Carta(valor='8', pao='Corazóns', nome='Un', simbolo='A')
        self.assertTrue(c1 >= c2)
        self.assertTrue(c3 >= c2)
    def test_ge_ok_distintos(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='1', pao='Picas', nome='Unn', simbolo='Ah')
        c3 = Carta(valor='8', pao='Corazóns', nome='Un', simbolo='A')
        self.assertTrue(c1 >= c2)
        self.assertTrue(c3 >= c2)
    def test_ge_erro_iguais(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='2', pao='Corazóns', nome='Un', simbolo='A')
        self.assertFalse(c1 >= c2)
    def test_ge_erro_distintos(self):
        c1 = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        c2 = Carta(valor='4', pao='Picas', nome='Unn', simbolo='Ah')
        self.assertFalse(c1 >= c2)

    def test_hash(self):
        c = Carta(valor='1', pao='Corazóns', nome='Un', simbolo='A')
        self.assertEqual(hash(c), hash((c.get_simbolo(), c.get_nome(), c.get_valor(), c.get_pao())))

    # máxicos #

# para que corran os tests
unittest.main()

# ------------------------------------------------------
