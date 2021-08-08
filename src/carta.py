#! /usr/bin/python3
#-*- coding: utf-8 -*-
# ------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	07/08/2021 22:03:25
#+ Editado:	08/08/2021 12:21:31
# ------------------------------------------------

from typing import Optional

#  
class Carta:
    valor: str
    pao: str
    nome: str
    simbolo: Optional[str]

    # constructor
    def __init__(self, valor, pao, nome, simbolo = None) -> None:
        self.valor = valor
        self.pao = pao
        self.nome = nome
        self.simbolo = simbolo

    # getters
    # 
    def get_valor(self) -> str:
        return self.valor

    # 
    def get_pao(self) -> str:
        return self.pao

    # 
    def get_nome(self) -> str:
        return self.nome

    # 
    def get_simbolo(self) -> str:
        return self.simbolo
    # getters #

    # setters #
    # 
    def set_valor(self, novo_valor) -> bool:
        try:
            self.valor = novo_valor
        except:
            return False
        else:
            return True

    # 
    def set_pao(self, novo_pao) -> bool:
        try:
            self.pao = novo_pao
        except:
            return False
        else:
            return True

    # 
    def set_nome(self, novo_nome) -> bool:
        try:
            self.nome = novo_nome
        except:
            return False
        else:
            return True

    # 
    def set_simbolo(self, novo_simbolo) -> bool:
        try:
            self.simbolo = novo_simbolo
        except:
            return False
        else:
            return True
    # setters #

    # máxicos
    # operación str() e print()
    def __str__(self) -> str:
        if self.pao == None:
            return f'{self.simbolo}: {self.nome}({self.valor})'
        else:
            return f'{self.simbolo}: {self.nome}({self.valor}) de {self.pao}'

    # Operación len()
    def __len__(self) -> int:
        return self.valor

    # Operador ==
    def __eq__(self, outra) -> bool:
        if self.valor == outra.valor:
            return True
        return False
        
    # Operación !=
    def __ne__(self, outra) -> bool:
        if self.valor == outra.valor:
            return True
        return False

    # Operación <
    def __lt__(self, outra) -> bool:
        if self.valor < outra.valor:
            return True
        return False

    # Operación >
    def __gt__(self, outra) -> bool:
        if self.valor > outra.valor:
            return True
        return False

    # Operación <=
    def __le__(self, outra) -> bool:
        if self.valor <= outra.valor:
            return True
        return False
    
    # Operación >=
    def __ge__(self, outra) -> bool:
        if self.valor >= outra.valor:
            return True
        return False
    # máxicos #
# ------------------------------------------------
