#! /usr/bin/python3
#-*- coding: utf-8 -*-
# ------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	07/08/2021 22:03:25
#+ Editado:	07/08/2021 22:27:06
# ------------------------------------------------
class Carta:
    valor: str
    pao: str
    nome: str

    # constructor
    def __init__(self, valor, pao, nome) -> None:
        self.valor = valor
        self.pao = pao
        self.nome = nome

    # getters
    def get_valor(self) -> str:
        return self.valor

    def get_pao(self) -> str:
        return self.pao

    def get_nome(self) -> str:
        return self.nome
    # getters #

    # setters #
    def set_valor(self, novo_valor) -> bool:
        try:
            self.valor = novo_valor
        except:
            return False
        else:
            return True

    def set_pao(self, novo_pao) -> bool:
        try:
            self.pao = novo_pao
        except:
            return False
        else:
            return True

    def set_nome(self, novo_nome) -> bool:
        try:
            self.nome = novo_nome
        except:
            return False
        else:
            return True
    # setters #
# ------------------------------------------------
