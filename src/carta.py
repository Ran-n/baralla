#! /usr/bin/python3
#-*- coding: utf-8 -*-
# ------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	07/08/2021 22:03:25
#+ Editado:	07/08/2021 22:09:39
# ------------------------------------------------
class Carta:
    valor: str
    pao: str

    # constructor
    def __init__(self, valor, pao) -> None:
        self.valor = valor
        self.pao = pao

    def get_valor(self) -> str:
        return self.valor

    def get_pao(self) -> str:
        return self.pao

    def set_valor(self, novo_valor) -> bool:
        try:
            self.valor = novo_valor
        except:
            return False
        finally:
            return True

    def set_pao(self, novo_pao) -> bool:
        try:
            self.pao = novo_pao
        except:
            return False
        finally:
            return True
# ------------------------------------------------
