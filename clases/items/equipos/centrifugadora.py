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
    


def definir_centrifugadora(equipos: list) -> Centrifugadora:

    # Se pasa la lista con equipo anteriormente definido

    nombre = input('(-1) para cancelar la operación | Introduzca el nombre del equipo: ')


    if nombre == '-1':

        print('Cancelando operación...')
        return '-1'


    # Comprobramos que el nombre introducido forma parte o no
    # de equipamiento anteriormente definido


    for equipo in equipos:

        if nombre.lower() == equipo.nombre:

            print('Equipo anteriormente definido. Extrayendo copia...')

            return equipo
        
    
    rpm_max = pedir_int_entre_valores('Introduce las RPM máximas de la centrifugadora: ', 1, 100000)

    if rpm_max == '-1':

        print('Cancelando operación...')
        return '-1'

    return Centrifugadora(nombre.lower(), rpm_max)   # Todos los nombres serán puesto a lower