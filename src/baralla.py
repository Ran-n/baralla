#! /usr/bin/python3
#-*- coding: utf-8 -*-
# -------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	07/08/2021 22:09:00
#+ Editado:	11/08/2021 12:14:45
# -------------------------------------------------

import random
import secrets
from typing import Optional, List

from src.carta import Carta

from src.excepcions import PosicionInexistente, CartaInexistente, BarallaBaleira

# 
class Baralla:
    __nome: Optional[str]
    __preset: Optional[str]
    __cartas: Optional[List[str]]

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

    # 
    def __eliminar_aux(self, atrib, valor_atrib) -> list:
        indices = []
        for idx, ele in enumerate(self.__cartas):
            if atrib == 'valor':
                if ele.get_valor() == valor_atrib:
                    indices.append(idx)
            elif atrib == 'pao':
                if ele.get_pao() == valor_atrib:
                    indices.append(idx)
            elif atrib == 'nome':
                if ele.get_nome() == valor_atrib:
                    indices.append(idx)
            elif atrib == 'simbolo':
                if ele.get_simbolo() == valor_atrib:
                    indices.append(idx)
        return indices

    #
    def eliminar_valor(self, valor: str) -> bool:
        try:
            for indice in self.__eliminar_aux('valor', valor)[::-1]:
                self.eliminar_index(indice)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    # 
    def eliminar_pao(self, pao: str) -> bool:
        try:
            for indice in self.__eliminar_aux('pao', pao)[::-1]:
                self.eliminar_index(indice)
        except Exception as e:
            print(e)
            return False
        else:
            return True
    #
    def eliminar_nome(self, nome: str) -> bool:
        try:
            for indice in self.__eliminar_aux('nome', nome)[::-1]:
                self.eliminar_index(indice)
        except Exception as e:
            print(e)
            return False
        else:
            return True
    #
    def eliminar_simbolo(self, simbolo: str) -> bool:
        try:
            for indice in self.__eliminar_aux('simbolo', simbolo)[::-1]:
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
    def sacar_carta(self, aleatoria: bool) -> Carta:
        try:
            if aleatoria:
                # collemos unha carta aleatoria
                carta = secrets.choice(self.get_cartas())
            else:
                # collemos a primeira carta da lista
                carta = self.get_carta(0)
            # eliminamola da baralla
            self.eliminar_obx(carta)
        except IndexError:
            raise BarallaBaleira()
        except PosicionInexistente:
            raise BarallaBaleira()
        except:
            raise
        else:
            return carta
# -------------------------------------------------
