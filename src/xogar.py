#! /usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------
#+ Autor:	Ran#
#+ Creado:	10/08/2021 21:11:45
#+ Editado:	11/08/2021 13:07:52
# --------------------------------------------

# CONTEXTO patrón estratexia #

from src.excepcions import NonHerda
from src.xogo import XogarEstratexia

class Xogar:
    def __init__(self, estratexia: XogarEstratexia):
        if isinstance(estratexia, XogarEstratexia):
            self.estratexia = estratexia
        else:
            raise NonHerda(XogarEstratexia.__name__)

    def xogo(self):
        return self.estratexia.xogo()

# --------------------------------------------
