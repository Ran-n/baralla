#! /usr/bin/python3
#-*- encoding: utf-8 -*-
# ----------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	10/08/2021 20:58:40
#+ Editado:	11/08/2021 13:50:52
# ----------------------------------------------------

# ESTRATEXIA CONCRETA patrón estratexia #

from src.xogo import XogarEstratexia
from src.baralla import Baralla

class CartaAltaEstratexia(XogarEstratexia):
    def xogo(self, baralla = None, puntos = 0, num_xogo = 1) -> None:
        # crear unha baralla
        if not baralla:
            b = Baralla(preset='castela')
        else:
            b = baralla

        print()
        print(f'Xogo #{num_xogo} ----------')
        # sacar carta aleatoria
        c1 = b.sacar_carta(True)
        print(f'* A túa carta é *\n{c1}\n')
        while True:
            resposta = input('A seguinte será maior(>), menor(<) ou igual(=)?: ')
            print()
            if resposta in ['<', '>', '=']:
                print('-----------------------------------------')
                c2 = b.sacar_carta(True)
                if any([
                        c1 < c2 and resposta == '>',
                        c1 > c2 and resposta == '<',
                        c1 == c2 and resposta == '=',
                        ]):
                    print('ACERTACHES!')
                    puntos += 1
                else:
                    print('ERRACHES :(')
                print()
                print(f'* A segunda carta era *\n{c2}')
                print()
                while True:
                    sair = input('Continuar?[S/n]: ').lower()
                    if sair in ['s', 'n', '']:
                        break
                if sair == 'n':
                    print()
                    print(f'* Felicidades, conseguiches unha puntaxes de {puntos}! *')
                    break
                else:
                    self.xogo(b, puntos, num_xogo+1)
                    break
# ----------------------------------------------------
