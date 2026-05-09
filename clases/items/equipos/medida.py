from ..equipo import Equipo
from typing import Any, Optional, List
from funciones import *

import copy

class EquipoMedida(Equipo):

    def __init__(self, nombre: str, error_medida: float):
        
        super().__init__(nombre)
        self.error_medida: float = error_medida


    def __str__(self) -> str:
        return super().__str__() + f" | Error: ±{self.error_medida}"
    

    def __eq__(self, other: Any) -> bool:

        if isinstance(other, EquipoMedida):

            return super().__eq__(other) and self.error_medida == other.error_medida
        
        return False
    

# Equipos es la lista extraída de nuestro archivo pickle
def definir_equipo_medida(equipos: List[Any]) -> Optional[EquipoMedida]:

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
        
    
    error_medida = pedir_error_medida('(-1) para cancelar la operación | Introduzca el error de medida (±): ')

    if error_medida is None:

        return None
    
    return EquipoMedida(nombre.lower(), error_medida)
        

def pedir_error_medida(frase: str) -> Optional[float]:

    while True:

        print(frase, end='')

        valor_input = input()

        if valor_input == '-1':

            return None
        
        try:

            valor_final = float(valor_input)

            if valor_final < 0:

                print('Error. Introduzca un valor positivo.')

            else:

                return valor_final

        except ValueError:

            print('Error. Introduzca un valor numérico válido.')
