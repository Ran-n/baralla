#! /usr/bin/python3
#-*- encoding: utf-8 -*-
# -------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	09/08/2021 22:42:58
#+ Editado:	09/08/2021 23:10:48
# -------------------------------------------------

class PosicionInexistente(Exception):
    pass
    """
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('función str')
        if self.message:
            return '{0}'.format(self.message)
        else:
            return 'has been raised'
    """

class CartaInexistente(Exception):
    pass

class BarallaBaleira(Exception):
    pass
# -------------------------------------------------
