from ..item import Item

from funciones import *

class Equipo(Item):

    dicc_estados = {True: "Buen estado", False: "Defectuoso"}

    def __init__(self, nombre: str):

        super().__init__(nombre)

        # True -> Buen estado | False -> Defectuoso

        self.estado = True
        # El estado PODRÁ cambiar después de una sesión


    def __str__(self):

        txt_estado = type(self).dicc_estados.get(self.estado, "Desconocido") # Evitar errores

        return super().__str__() + f" | Estado: {txt_estado}"
    

    def __eq__(self, other):

        if isinstance(other, Equipo):

            return super().__eq__(other) and self.estado == other.estado
        
        return False
    

# equipos es la lista extraída de nuestro archivo pickle
def definir_equipamiento(equipos: list) -> Equipo:

    # Se pasa la lista con equipo anteriormente definido

    nombre = input('(-1) para cancelar la operación | Introduzca el nombre del equipo: ')

    # Comprobramos que el nombre introducido forma parte o no
    # de equipamiento anteriormente definido

    for equipo in equipos:

        if equipo.nombre.lower() == nombre:

            print('Equipo anteriormente definido. Extrayendo copia...')

            return equipo

    if nombre == '-1':

        return '-1' 
    
    return Equipo(nombre.lower())   # Todos los nombres serán puesto a lower
                                    # para evitar errores


# En esta función controlamos la cantidad que se importara

def importar_equipamiento(equipos) -> tuple:

    equipo = definir_equipamiento(equipos)

    if equipo == '-1':

        print('Cancelando operación...')
        return None


    copias = pedir_int('(-1) para cancelar la operación | Introduzca la cantidad: ')


    if copias == '-1':

        print('Cancelando operación...')
        return None
    

    return (equipo, copias) # Tupla para añadir al inventario