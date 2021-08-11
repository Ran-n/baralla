#! /usr/bin/python3
#-*- encoding: utf-8 -*-
# ------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	10/08/2021 20:52:22
#+ Editado:	10/08/2021 21:15:04
# ------------------------------------------------

# INTERFAZ patrón estratexia #

from abc import ABC, abstractmethod

class XogarEstratexia(ABC):
    @abstractmethod
    def crear_baralla(self):
        pass

# ------------------------------------------------
