#! /usr/bin/python3
#-*- coding: utf-8 -*-
# -------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	07/08/2021 22:09:00
#+ Editado:	08/08/2021 00:10:46
# -------------------------------------------------

import random
import secrets
from typing import Optional

try:
    from carta import Carta
except:
    from .carta import Carta

# 
class Baralla:
    nome: Optional[str]
    cartas: Optional[list]

    # constructor
    def __init__(self, nome= '', cartas = []) -> None:
        self.nome = nome
        self.cartas = cartas

    # getters
    # 
    def get_nome(self) -> str:
        return self.nome

    #
    def get_cartas(self) -> list:
        return self.cartas

    # 
    def get_carta(self, posicion) -> Carta:
        try:
            return self.cartas[posicion]
        except IndexError:
            # xFCR crear clase excepción
            raise Exception('Posición inexistente na baralla')
        else:
            return True
    # getters #

    # setters
    #
    def set_nome(self, novo_nome) -> bool:
        try:
            self.nome = novo_nome
        except:
            return False
        else:
            return True

    # 
    def set_cartas(self, novas_cartas) -> bool:
        try:
            self.cartas = novas_cartas
        except:
            return False
        else:
            return True
    # setters #

    # máxicos
    # 
    def __len__(self) -> int:
        return len(self.cartas)

    #
    def __str__(self) -> str:
        saida = 'Baralla {}'.format(self.nome)
        # se non ten cartas que poña que non as ten
        if len(self.cartas) == 0:
            saida += '\nBaleira'

        for ele in self.cartas:
            saida += '\n{}'.format(str(ele))
        return saida
    # máxicos #

    # 
    def resetear_baralla(self) -> bool:
        try:
            self.cartas.clear()
        except:
            return False
        else:
            return True

    # 
    def engadir(self, pao, valor, nome, simbolo=None) -> bool:
        self.cartas.append(Carta(pao=pao, valor=valor, nome=nome, simbolo=simbolo))

    # 
    def eliminar_index(self, posicion) -> bool:
        try:
            self.cartas.pop(posicion)
        except IndexError:
            # xFCR crear clase excepción
            raise Exception('Posición inexistente na baralla')
        else:
            return True

    # 
    def eliminar_obx(self, carta) -> bool:
        try:
            self.cartas.remove(carta)
        except ValueError:
            # xFCR crear clase excepción
            raise Exception('Posición inexistente na baralla')
        else:
            return True

    # elimina as cartas valoradas en 0
    def eliminar_comodins(self) -> bool:
        try:
            for idx, ele in enumerate(self.cartas):
                if ele.get_valor == '0':
                    self.eliminar_index(idx)
        except:
            return False
        else:
            return True

    #
    def barallar(self) -> bool:
        random.shuffle(self.cartas)        

    # 
    def sacar_carta(self) -> Carta:
        # collemos unha carta aleatoria
        carta = secrets.choice(self.cartas)
        # eliminamola da baralla
        self.eliminar_obx(carta)
        return carta
    # 
    def set_baralla_castela(self) -> bool:
        self.resetear_baralla()

        paos = ['Espadas', 'Copas', 'Ouros', 'Bastos']
        valores = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10' ,'11', '12']
        nomes = ['As', 'Dous', 'Tres', 'Catro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Sota', 'Cabalo', 'Rey']
        #simbolos = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '🤺', '🐴', '👑']
        simbolos = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'S', 'C', 'R']
        #joker = '🃏'
        simbolo_comodin = '*'

        try:
            self.engadir(pao=None, valor='0', nome='Comodín', simbolo=simbolo_comodin)
            self.engadir(pao=None, valor='0', nome='Comodín', simbolo=simbolo_comodin)
            for pao in paos:
                for valor, nome, simbolo in zip(valores, nomes, simbolos):
                    self.engadir(pao=pao, valor=valor, nome=nome, simbolo=simbolo)
        except:
            raise
            return False
        else:
            return True

    #
    def set_baralla_poker(self) -> bool:
        self.resetear_baralla()

        paos = ['Diamantes', 'Tréboles', 'Corazóns', 'Picas']
        valores = ['1', '2', '3', '4' ,'5', '6', '7', '8', '9', '10', '11', '12', '13']
        nomes = ['As', 'Dous', 'Tres', 'Catro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Sota', 'Dama', 'Rei']
        simbolos = ['A', '2', '3', '4' ,'5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        simbolo_comodin = '*'

        try:
            self.engadir(pao=None, valor='0', nome='Comodín', simbolo=simbolo_comodin)
            self.engadir(pao=None, valor='0', nome='Comodín', simbolo=simbolo_comodin)
            for pao in paos:
                for valor, nome, simbolo in zip(valores, nomes, simbolos):
                    self.engadir(pao=pao, valor=valor, nome=nome, simbolo=simbolo)
        except:
            return False
        else:
            return True
        
# -------------------------------------------------
