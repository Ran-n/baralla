#! /usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------
#+ Autor:	Ran#
#+ Creado:	10/08/2021 21:11:45
#+ Editado:	12/08/2021 00:48:05
# --------------------------------------------

# CONTEXTO patrón estratexia #

from src.excepcions import NonHerda
from src.xogo import XogarEstratexia

class Xogar:
    def __init__(self, estratexia: XogarEstratexia) -> None:
        if isinstance(estratexia, XogarEstratexia):
            self.estratexia = estratexia
        else:
            raise NonHerda(XogarEstratexia.__name__)

    def xogo(self) -> None:
        return self.estratexia.xogo()

# --------------------------------------------
