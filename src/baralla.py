#! /usr/bin/python3
#-*- coding: utf-8 -*-
# -------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	07/08/2021 22:09:00
#+ Editado:	07/08/2021 22:51:30
# -------------------------------------------------

from typing import Optional

try:
    from carta import Carta
except:
    from .carta import Carta

class Baralla:
    cartas: Optional[list]

    # constructor
    def __init__(self, cartas = []) -> None:
        self.cartas = cartas

    # getters
    def get_cartas(self) -> list:
        return self.cartas
    # getters #

    # setters
    def set_cartas(self, novas_cartas) -> bool:
        try:
            self.cartas = novas_cartas
        except:
            return False
        else:
            return True
    # setters #
    def engadir_carta(self, pao, valor, nome, simbolo=None) -> bool:
        self.cartas.append(Carta(pao=pao, valor=valor, nome=nome, simbolo=simbolo))

    def set_baralla_castela(self) -> bool:
        paos = ['Espadas', 'Copas', 'Ouros', 'Bastos']
        valores = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10' ,'11', '12']
        nomes = ['As', 'Dous', 'Tres', 'Catro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Sota', 'Cabalo', 'Rey']
        simbolos = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '🤺', '🐴', '👑']
        joker = '🃏'

        try:
            self.engadir_carta(pao=None, valor='0', nome='Comodín', simbolo=joker)
            self.engadir_carta(pao=None, valor='0', nome='Comodín', simbolo=joker)
            for pao in paos:
                for valor, nome, simbolo in zip(valores, nomes, simbolos):
                    self.engadir_carta(pao=pao, valor=valor, nome=nome, simbolo=simbolo)
        except:
            return False
        else:
            return True
        
# -------------------------------------------------
