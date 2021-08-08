#! /usr/bin/python3
#-*- coding: utf-8 -*-
# ------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	07/08/2021 22:03:25
#+ Editado:	08/08/2021 14:15:22
# ------------------------------------------------

from typing import Optional

#  
class Carta:
    __valor: str
    __pao: str
    __nome: str
    __simbolo: Optional[str]

    # constructor
    def __init__(self, valor, pao, nome, simbolo = None) -> None:
        self.__valor = valor
        self.__pao = pao.capitalize()
        self.__nome = nome.capitalize()
        self.__simbolo = simbolo

    # getters
    # 
    def get_valor(self) -> str:
        return self.__valor

    # 
    def get_pao(self) -> str:
        return self.__pao

    # 
    def get_nome(self) -> str:
        return self.__nome

    # 
    def get_simbolo(self) -> str:
        return self.__simbolo
    # getters #

    # setters #
    # 
    def set_valor(self, novo_valor) -> bool:
        try:
            self.__valor = novo_valor
        except:
            return False
        else:
            return True

    # 
    def set_pao(self, novo_pao) -> bool:
        try:
            self.__pao = novo_pao
        except:
            return False
        else:
            return True

    # 
    def set_nome(self, novo_nome) -> bool:
        try:
            self.__nome = novo_nome
        except:
            return False
        else:
            return True

    # 
    def set_simbolo(self, novo_simbolo) -> bool:
        try:
            self.__simbolo = novo_simbolo
        except:
            return False
        else:
            return True
    # setters #

    # máxicos
    # operación str() e print()
    def __str__(self) -> str:
        saida = ''
        if self.__simbolo:
            saida += 'Símbolo: {}'.format(self.__simbolo)

        if self.__nome:
            saida += '\nNome:\t {}'.format(self.__nome)

        if self.__valor:
            saida += '\nValor:\t {}'.format(self.__valor)

        if self.__pao:
            saida += '\nPao:\t {}'.format(self.__pao)

        #return f'{self.simbolo}: {self.nome}({self.valor}) de {self.pao}'
        if saida.startswith('\n'): return saida.replace('\n', '', 1)
        return saida

    # Operación len()
    def __len__(self) -> int:
        return self.__valor

    # Operador ==
    def __eq__(self, outra) -> bool:
        if self.__valor == outra.valor:
            return True
        return False
        
    # Operación !=
    def __ne__(self, outra) -> bool:
        if self.__valor == outra.valor:
            return True
        return False

    # Operación <
    def __lt__(self, outra) -> bool:
        if self.__valor < outra.valor:
            return True
        return False

    # Operación >
    def __gt__(self, outra) -> bool:
        if self.__valor > outra.valor:
            return True
        return False

    # Operación <=
    def __le__(self, outra) -> bool:
        if self.__valor <= outra.valor:
            return True
        return False
    
    # Operación >=
    def __ge__(self, outra) -> bool:
        if self.__valor >= outra.valor:
            return True
        return False
    # máxicos #
# ------------------------------------------------
