from ..consumible import Consumible

from funciones import *

class ReactivoSolido(Consumible):

    def __init__(self, nombre, inventario, cantidad, lote, masa: float):
        
        super().__init__(nombre, inventario, cantidad, lote)
        self.masa = masa


    def __str__(self):
        return super().__str__() + f" | Masa: {self.masa}g"
    

    def __eq__(self, other):

        if isinstance(other, ReactivoSolido):

            return super().__eq__(other) and self.masa == other.masa

        return False