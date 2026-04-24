from ..equipo import Equipo

from funciones import *

class EquipoTermico(Equipo):

    def __init__(self, nombre, temp_max: float, temp_min: float):
        
        super().__init__(nombre)
        self.temp_max = temp_max
        self.temp_min = temp_min

    def __str__(self):
        return super().__str__() + f" | Rango [{self.temp_min} °C, {self.temp_max} °C]"
    
    def __eq__(self, other):

        if isinstance(other, EquipoTermico):

            return super().__eq__(other) and self.temp_max == other.temp_max and self.temp_min == other.temp_min
        
        return False
    
    
def verificar_rango_temperatura(temp_max, temp_min):

    if temp_max <= temp_min:

        raise ValueError("La temperatura máxima no puede ser menor que la mínima.")