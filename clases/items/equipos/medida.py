from ..equipo import Equipo

from funciones import *

import copy

class EquipoMedida(Equipo):

    def __init__(self, nombre, error_medida: float):
        
        super().__init__(nombre)
        self.error_medida = error_medida


    def __str__(self):
        return super().__str__() + f" | Error: ±{self.error_medida}"
    

    def __eq__(self, other):

        if isinstance(other, EquipoMedida):

            return super().__eq__(other) and self.error_medida == other.error_medida
        
        return False
    

# Equipos es la lista extraída de nuestro archivo pickle
def definir_equipo_medida(equipos: list) -> EquipoMedida:

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

    if error_medida == '-1':

        return None
    
    return EquipoMedida(nombre.lower(), error_medida)
        

def pedir_error_medida(frase: str) -> float:

    while True:

        print(frase, end='')

        error_medida = input()

        if error_medida == '-1':

            return None
        
        try:

            error_medida = float(error_medida)

            if error_medida < 0:

                print('Error. Introduzca un valor positivo.')

            else:

                return error_medida

        except ValueError:

            print('Error. Introduzca un valor numérico válido.')
