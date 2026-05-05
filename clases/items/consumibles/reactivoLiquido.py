from ..consumible import Consumible
from ..lote import Lote

from funciones import *

class ReactivoLiquido(Consumible):

    def __init__(self, nombre, inventario, cantidad, lote, volumen: float):

        super().__init__(nombre, inventario, cantidad, lote)
        self.volumen = volumen


    def __str__(self):
        return super().__str__() + f" | Vol: {self.volumen} ml"
    
    def __eq__(self, other):

        if isinstance(other, ReactivoLiquido):

            return self.nombre.lower() == other.nombre.lower() and self.volumen == other.volumen \
                and self._Consumible__lote == other._Consumible__lote

        return False
    

def importar_reactivo_liquido(consumibles: list, lote: Lote):

    pass