#! /usr/bin/python3
#-*- encoding: utf-8 -*-
# ----------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	10/08/2021 20:58:40
#+ Editado:	12/08/2021 00:43:38
# ----------------------------------------------------

# ESTRATEXIA CONCRETA patrón estratexia #

from termcolor import cprint

from src.xogo import XogarEstratexia
from src.baralla import Baralla

class CartaAltaEstratexia(XogarEstratexia):
    def __sacar_acerto(self, puntos, num_xogo):
        return int((puntos/num_xogo) * 100)
    
    def __imprimir_puntaxe(self, puntos, acerto, fin=False):
        if fin:
            cprint('\n* Felicidades, conseguiches *', 'white', attrs=['bold'])
        else:
            cprint('* ----- Marcador ----- *', 'white', attrs=['bold'])

        if puntos == 1:
            cprint(f'Puntaxe:\t{puntos} pto\nAcerto: \t{acerto} %', 'white', attrs=['bold'])
        else:
            cprint(f'Puntaxe:\t{puntos} ptos\nAcerto: \t{acerto} %', 'white', attrs=['bold'])


    def xogo(self, baralla = None, puntos = 0, num_xogo = 1) -> None:
        # crear unha baralla se non mete baralla ou a metida está baleira
        if not baralla:
            cprint('* Creando unha nova baralla *', 'yellow', attrs=['bold'])
            b = Baralla(preset='castela')
        else:
            b = baralla

        print()
        print(f'Xogo #{num_xogo} ----------')
        # sacar carta aleatoria
        c1 = b.sacar_carta(True)
        print('* A túa carta é *')
        cprint(f'{c1}', 'cyan', attrs=['bold'])
        while True:
            resposta = input('A seguinte será maior(>), menor(<) ou igual(=)?: ')

            if resposta == '.':
                self.__imprimir_puntaxe(puntos, self.__sacar_acerto(puntos, num_xogo))

            if resposta in ['<', '>', '=']:
                print('\n-----------------------------------------')
                c2 = b.sacar_carta(True)
                if any([
                        c1 < c2 and resposta == '>',
                        c1 > c2 and resposta == '<',
                        c1 == c2 and resposta == '=',
                        ]):
                    cprint('ACERTACHES!', 'green', attrs=['bold'])
                    puntos += 1
                else:
                    cprint('ERRACHES :(', 'red', attrs=['bold'])
                print()
                print('* A segunda carta era *')
                cprint(f'{c2}', 'cyan', attrs=['bold'])
                while True:
                    sair = input('Continuar?[S/n]: ').lower()
                    if sair in ['s', 'n', '']:
                        break
                    if sair == '.':
                        self.__imprimir_puntaxe(puntos, self.__sacar_acerto(puntos, num_xogo))
                        
                if sair == 'n':
                    self.__imprimir_puntaxe(puntos, self.__sacar_acerto(puntos, num_xogo), True)
                    break
                else:
                    self.xogo(b, puntos, num_xogo+1)
                    break
# ----------------------------------------------------
