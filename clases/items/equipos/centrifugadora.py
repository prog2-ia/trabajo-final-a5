from ..equipo import Equipo

from funciones import *

class Centrifugadora(Equipo):

    def __init__(self, nombre, estado, rpm_max: int):

        super().__init__(nombre, estado)
        self.rpm_max = rpm_max

    def __str__(self):
        return super().__str__() + f" | RPM Max: {self.rpm_max}"