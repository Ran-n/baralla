#! /usr/bin/python3
#-*- coding: utf-8 -*-
# -------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	07/08/2021 22:09:00
#+ Editado:	09/08/2021 23:18:08
# -------------------------------------------------

import random
import secrets
from typing import Optional

from carta import Carta

from excepcions import PosicionInexistente, CartaInexistente, BarallaBaleira

# 
class Baralla:
    __nome: Optional[str]
    __preset: Optional[str]
    __cartas: Optional[list]

    # constructor
    def __init__(self, nome='', preset=None, cartas=None) -> None:
        self.__nome = nome
        self.__preset = preset
        self.__cartas = cartas

        # isto ten que ir antes porque se mete o preset na declaración da erro
        if not cartas: self.__cartas = []
        # se meteu preset tentamolo
        if self.__preset: self.set_preset(self.__preset)

    # getters
    # 
    def get_nome(self) -> str:
        return self.__nome

    # 
    def get_preset(self) -> str:
        return self.__preset

    #
    def get_cartas(self) -> list:
        return self.__cartas

    # 
    def get_carta(self, posicion) -> Carta:
        try:
            return self.get_cartas()[posicion]
        except IndexError:
            raise PosicionInexistente(f'Posición #{posicion}')
        except:
            raise
    # getters #

    # setters
    #
    def set_nome(self, novo_nome) -> bool:
        try:
            self.__nome = novo_nome
        except:
            return False
        else:
            return True

    # crea barallas predefinidas como a de poker ou a castelá
    def set_preset(self, tipo) -> bool:
        self.resetear_baralla()

        if tipo.lower() == 'castela':
            self.__preset = 'castela'
            paos = ['Espadas', 'Copas', 'Ouros', 'Bastos']
            valores = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10' ,'11', '12']
            nomes = ['As', 'Dous', 'Tres', 'Catro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Sota', 'Cabalo', 'Rey']
            #simbolos = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '🤺', '🐴', '👑']
            simbolos = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'S', 'C', 'R']
            #joker = '🃏'
            simbolo_comodin = '*'

        elif tipo.lower() == 'poker':
            self.__preset = 'poker'
            paos = ['Diamantes', 'Tréboles', 'Corazóns', 'Picas']
            valores = ['1', '2', '3', '4' ,'5', '6', '7', '8', '9', '10', '11', '12', '13']
            nomes = ['As', 'Dous', 'Tres', 'Catro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Sota', 'Dama', 'Rei']
            simbolos = ['A', '2', '3', '4' ,'5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            simbolo_comodin = '*'
        else:
            return False

        try:
            self.engadir(Carta(pao=None, valor='0', nome='Comodín', simbolo=simbolo_comodin))
            self.engadir(Carta(pao=None, valor='0', nome='Comodín', simbolo=simbolo_comodin))
            for pao in paos:
                for valor, nome, simbolo in zip(valores, nomes, simbolos):
                    self.engadir(Carta(pao=pao, valor=valor, nome=nome, simbolo=simbolo))
        except:
            raise
            return False
        else:
            return True

    # 
    def set_cartas(self, novas_cartas, eliminar=False) -> bool:
        try:
            if eliminar: self.resetear_baralla()
            self.__cartas = novas_cartas
        except:
            return False
        else:
            return True
    # setters #

    # máxicos
    # 
    def __len__(self) -> int:
        return len(self.get_cartas())

    #
    def __str__(self) -> str:
        saida = 'Baralla {}\n-------------------'.format(self.get_nome())
        # se non ten cartas que poña que non as ten
        if len(self.get_cartas()) == 0:
            saida += '\nBaleira'
        else:
            for idx, ele in enumerate(self.get_cartas()):
                saida += '\n#{}\n{}\n'.format(idx+1, str(ele))
            saida = saida[:-1]
        return saida

    # 
    def __hash__(self) -> int:
        hashes_cartas = []
        for carta in self.get_cartas():
            hashes_cartas.append(hash(carta))

        return hash((self.get_nome(), self.get_preset(), sum(hashes_cartas)))
    # máxicos #

    # 
    def resetear_baralla(self) -> bool:
        try:
            self.__cartas.clear()
        except Exception as e:
            print(e)
            return False
        else:
            return True

    # 
    def engadir(self, carta: Carta) -> bool:
        try:
            self.__cartas.append(carta)
        except:
            raise
        else:
            return True

    # 
    def eliminar_index(self, posicion) -> bool:
        try:
            self.__cartas.pop(posicion)
        except IndexError:
            raise PosicionInexistente(f'Posición #{posicion}')
        except Exception as e:
            print(e)
            return False
        else:
            return True

    # 
    def eliminar_obx(self, carta) -> bool:
        try:
            self.__cartas.remove(carta)
        except ValueError:
            raise CartaInexistente('Carta → {}'.format(carta.replace('\n',', ')))
        except:
            raise
        else:
            return True

    # elimina as cartas valoradas en 0
    # xFCR: mellorar
    def eliminar_comodins(self) -> bool:
        try:
            indices = []
            for idx, ele in enumerate(self.__cartas):
                if ele.get_valor() == '0':
                    indices.append(idx)
            for indice in indices:
                self.eliminar_index(indice)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    #
    def barallar(self) -> bool:
        try:
            random.shuffle(self.__cartas)        
        except Exception as e:
            print(e)
            return False
        else:
            return True

    # sacaa de forma aleatoria
    def sacar_carta_aleatoria(self) -> Carta:
        try:
            # collemos unha carta aleatoria
            carta = secrets.choice(self.get_cartas())
            # eliminamola da baralla
            self.eliminar_obx(carta)
        except IndexError:
            raise BarallaBaleira()
        except:
            raise
        else:
            return carta

# -------------------------------------------------
