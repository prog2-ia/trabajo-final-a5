from ..item import Item
from typing import Any, Dict, Optional, List, Tuple

from funciones import *

import copy

class Equipo(Item):
    # Diccionario de clase para transformar el booleano del estado en texto legible
    dicc_estados: Dict[bool,str] = {True: "Buen estado", False: "Defectuoso"}

    def __init__(self, nombre: str):

        super().__init__(nombre)

        # True -> Buen estado | False -> Defectuoso

        self.estado: bool = True
        # El estado PODRÁ cambiar después de una sesión, cuando
        # los científicos devuelvan el equipo, se podrá marcar como defectuoso o no


    def __str__(self) -> str:
        # Recupera el texto de forma segura: si no existe, por defecto será 'Desconocido'
        txt_estado: str = type(self).dicc_estados.get(self.estado, "Desconocido") # Evitar errores

        return super().__str__() + f" | Estado: {txt_estado}"
    

    def __eq__(self, other: Any) -> bool:
        # Dos equipos son iguales si coincide su nombre (clase base) y su estado actual
        if isinstance(other, Equipo):

            return super().__eq__(other) and self.estado == other.estado
        
        return False
    

# Equipos es la lista extraída de nuestro archivo pickle
def definir_equipamiento(equipos: List[Any]) -> Optional[Equipo]:

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

    
    return Equipo(nombre.lower())   # Todos los nombres serán puesto a lower
                                    # para evitar errores


# En esta función controlamos la cantidad que se importara

def importar_equipamiento(equipo: Optional[Equipo]) -> Optional[Tuple[Equipo, int]]:

    if equipo is None:

        return None # Esto acabara el anadir_item, el cual mostrara el mensaje de cancelando operación
    
    # Bucle para solicitar cuántas unidades/copias de este equipo se van a aañadir
    while True:

        copias = pedir_int_entre_valores('(-1) para cancelar la operación | Introduzca la cantidad: ', 1, 999)

        if copias is None:

            return None
        
        else:
            # Retorna el formato estándar de inventario: una tupla (objeto, cantidad)
            return (equipo, copias)
        


def traer_equipamiento_definido(equipos: List[Any]) -> Optional[Equipo]:
    # Validación: si la lista histórica está vacía, no se puede importar nada
    if not equipos:

        print('No hay equipamiento anteriormente definido.')
        return None
    
    # Imprime la lista de equipos definidos numerada del 1 en adelante
    for indice, equipo in enumerate(equipos, start=1):

        print(f'[{indice}]\t-\t{str(equipo)}')

    # Pedimos el índice del equipo que se quiera importar
    equipamiento_elegido = pedir_int_entre_valores('(-1) para cancelar la operación | Introduzca el equipo a importar: ', 1, len(equipos))

    if equipamiento_elegido is None:

        return None
    # Retorna el objeto apuntado por el usuario (ajustando el desfase del start=1)
    return equipos[equipamiento_elegido - 1]