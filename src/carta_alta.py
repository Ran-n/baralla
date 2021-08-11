#! /usr/bin/python3
#-*- encoding: utf-8 -*-
# ----------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	10/08/2021 20:58:40
#+ Editado:	10/08/2021 21:32:56
# ----------------------------------------------------

# ESTRATEXIA CONCRETA patrón estratexia #

from src.xogo import XogarEstratexia
from src.baralla import Baralla

class CartaAltaEstratexia(XogarEstratexia):
    def crear_baralla(self):
        # crear unha baralla
        b = Baralla()

# ----------------------------------------------------
