#! /usr/bin/python3
#-*- encoding: utf-8 -*-
# ------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	10/08/2021 20:52:22
#+ Editado:	12/08/2021 00:47:44
# ------------------------------------------------

# INTERFAZ patrón estratexia #

from abc import ABC, abstractmethod

class XogarEstratexia(ABC):
    @abstractmethod
    def xogo(self) -> None:
        pass

# ------------------------------------------------
