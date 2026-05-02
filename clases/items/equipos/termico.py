from ..equipo import Equipo

from funciones import *

import copy

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
    

# Equipos es la lista extraída de nuestro archivo pickle
def definir_equipo_termico(equipos: list) -> EquipoTermico:

    # Se pasa la lista con equipo anteriormente definido

    nombre = input('(-1) para cancelar la operación | Introduzca el nombre del equipo: ')

    if nombre == '-1':

        return '-1' 

    # Comprobramos que el nombre introducido forma parte o no
    # de equipamiento anteriormente definido

    for equipo in equipos:

        if equipo.nombre.lower() == nombre:

            print('Equipo anteriormente definido. Extrayendo copia...')

            return copy.deepcopy(equipo)
        

def pedir_rango_temperatura():

    while True:

        temp_min = pedir_temperatura('Introduzca cualquier carácter para cancelar la operación | Introduzca la temperatura mínima (°C): ')

        if temp_min == '-1':

            return None
        

        temp_max = pedir_temperatura('Introduzca cualquier carácter para cancelar la operación | Introduzca la temperatura máxima (°C): ')

        if temp_max == '-1':

            return None
        
        try:

            verificar_rango_temperatura(temp_max, temp_min)

            return temp_max, temp_min

        except ValueError:

            print('Introduzca temperaturas mínimas y máximas válidas.')



# Como -1 puede ser una temperatura válida, hace falta una función de pedir float diferente a la
# establecida en funciones.py

def pedir_temperatura(frase: str) -> float:

    while True:

        print(frase, end='')

        # Usaremos caracteres para cancelar la función

        temperatura = input()

        if temperatura.isalpha():

            return None # Se devuelve un None, entonces la cadena de arrastrarlo hasta que
                        # anadir_item() lo verifique funcionara porque no se trata de un número

        try:

            return float(temperatura)
        
        except ValueError:

            print('Introduzca una temperatura válida.')