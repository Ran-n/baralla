#! /usr/bin/python3
#-*- encoding: utf-8 -*-
# ------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	10/08/2021 20:52:22
#+ Editado:	11/08/2021 13:06:43
# ------------------------------------------------

# INTERFAZ patrón estratexia #

from abc import ABC, abstractmethod

class XogarEstratexia(ABC):
    @abstractmethod
    def xogo(self):
        pass

# ------------------------------------------------
