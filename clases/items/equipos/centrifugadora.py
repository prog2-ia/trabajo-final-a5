from ..equipo import Equipo
from funciones import *
from typing import Any, Optional, List

import copy

class Centrifugadora(Equipo):

    def __init__(self, nombre: str, rpm_max: int):

        super().__init__(nombre)
        self.rpm_max: int = rpm_max

    def __str__(self) -> str:
        return super().__str__() + f" | RPM Max: {self.rpm_max}"
    
    def __eq__(self, other: Any) -> bool:

        if isinstance(other, Centrifugadora):

            return super().__eq__(other) and self.rpm_max == other.rpm_max
        
        return False
    


# Equipos es la lista extraída de nuestro archivo pickle
def definir_centrifugadora(equipos: List[Any]) -> Optional[Centrifugadora]:

    # Se pasa la lista con equipo anteriormente definido

    nombre = input('(-1) para cancelar la operación | Introduzca el nombre del equipo: ')

    if nombre == '-1':

        return None

    # Comprobramos que el nombre introducido forma parte o no
    # de equipamiento anteriormente definido

    for equipo in equipos:

        if equipo.nombre.lower() == nombre:

            print('Equipo anteriormente definido. Extrayendo copia...')

            return copy.deepcopy(equipo)
        
    
    rpm_max = pedir_int_entre_valores('(-1) para cancelar la operación | Introduzca las RPM máximas: ', 1, 1000000)

    if rpm_max is None:

        return None

    return Centrifugadora(nombre.lower(), rpm_max)   # Todos los nombres serán puesto a lower