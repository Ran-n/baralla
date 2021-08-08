#! /usr/bin/python3
#-*- coding: utf-8 -*-
# -------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	07/08/2021 22:09:00
#+ Editado:	08/08/2021 14:01:19
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
    preset: Optional[str]
    cartas: Optional[list]

    # constructor
    def __init__(self, nome='', preset=False, cartas=[]) -> None:
        self.nome = nome
        self.preset = preset
        self.cartas = cartas

        # se meteu preset tentamolo
        if self.preset:
            self.set_preset(self.preset)

    # getters
    # 
    def get_nome(self) -> str:
        return self.nome

    # 
    def get_preset(self) -> str:
        return self.preset

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
        except:
            return False
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

    # crea barallas predefinidas como a de poker ou a castelá
    def set_preset(self, tipo) -> bool:
        self.resetear_baralla()

        if tipo.lower() == 'poker':
            paos = ['Espadas', 'Copas', 'Ouros', 'Bastos']
            valores = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10' ,'11', '12']
            nomes = ['As', 'Dous', 'Tres', 'Catro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Sota', 'Cabalo', 'Rey']
            #simbolos = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '🤺', '🐴', '👑']
            simbolos = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'S', 'C', 'R']
            #joker = '🃏'
            simbolo_comodin = '*'

        elif tipo.lower() == 'castela':
            paos = ['Diamantes', 'Tréboles', 'Corazóns', 'Picas']
            valores = ['1', '2', '3', '4' ,'5', '6', '7', '8', '9', '10', '11', '12', '13']
            nomes = ['As', 'Dous', 'Tres', 'Catro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Sota', 'Dama', 'Rei']
            simbolos = ['A', '2', '3', '4' ,'5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            simbolo_comodin = '*'
        else:
            return False

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
        saida = 'Baralla {}\n-------------------'.format(self.nome)
        # se non ten cartas que poña que non as ten
        if len(self.cartas) == 0:
            saida += '\nBaleira'

        for idx, ele in enumerate(self.cartas):
            saida += '\n#{}\n{}\n'.format(idx+1, str(ele))
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
        except:
            return False
        else:
            return True

    # 
    def eliminar_obx(self, carta) -> bool:
        try:
            if not self.cartas.remove(carta):
                return False
        except ValueError:
            # xFCR crear clase excepción
            raise Exception('Posición inexistente na baralla')
        except:
            return False
        else:
            return True

    # elimina as cartas valoradas en 0
    # xFCR: mellorar
    def eliminar_comodins(self) -> bool:
        try:
            indices = []
            for idx, ele in enumerate(self.cartas):
                if ele.get_valor() == '0':
                    indices.append(idx)
            for indice in indices:
                self.eliminar_index(indice)
        except:
            return False
        else:
            return True

    #
    def barallar(self) -> bool:
        random.shuffle(self.cartas)        

    # sacaa de forma aleatoria
    def sacar_carta_aleatoria(self) -> Carta:
        # collemos unha carta aleatoria
        carta = secrets.choice(self.cartas)
        # eliminamola da baralla
        self.eliminar_obx(carta)
        return carta

# -------------------------------------------------
