from ..equipo import Equipo

from funciones import *

class Centrifugadora(Equipo):

    def __init__(self, nombre, rpm_max: int):

        super().__init__(nombre)
        self.rpm_max = rpm_max

    def __str__(self):
        return super().__str__() + f" | RPM Max: {self.rpm_max}"
    
    def __eq__(self, other):

        if isinstance(other, Centrifugadora):

            return super().__eq__(other) and self.rpm_max == other.rpm_max
        
        return False