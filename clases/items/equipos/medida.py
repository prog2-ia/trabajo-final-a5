from ..equipo import Equipo

from funciones import *

class EquipoMedida(Equipo):

    def __init__(self, nombre, estado, error_medida: float):
        
        super().__init__(nombre, estado)
        self.error_medida = error_medida


    def __str__(self):
        return super().__str__() + f" | Error: ±{self.error_medida}"
    

    def __eq__(self, other):

        if isinstance(other, EquipoMedida):

            return super().__eq__(other) and self.error_medida == other.error_medida
        
        return False