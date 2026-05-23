from ..equipo import Equipo
from funciones import *
from typing import Any, Optional, Tuple, List

import copy

class EquipoTermico(Equipo):

    def __init__(self, nombre: str, temp_max: float, temp_min: float):
        
        super().__init__(nombre)
        self.temp_max: float = temp_max
        self.temp_min: float = temp_min

    def __str__(self) -> str:
        return super().__str__() + f" | Rango [{self.temp_min} °C, {self.temp_max} °C]"
    
    def __eq__(self, other: Any) -> bool:
        # Verifica la igualdad basándose en el nombre (clase base) y los límites de temperatura
        if isinstance(other, EquipoTermico):

            return super().__eq__(other) and self.temp_max == other.temp_max and self.temp_min == other.temp_min
        
        return False
    
    


def verificar_rango_temperatura(temp_max: float, temp_min: float) -> None:
    # Límite superior es mayor que el inferior
    if temp_max <= temp_min:

        raise ValueError("La temperatura máxima no puede ser menor que la mínima.")
    

# Equipos es la lista extraída de nuestro archivo pickle
def definir_equipo_termico(equipos: List[Any]) -> Optional[EquipoTermico]:

    # Se pasa la lista con equipo anteriormente definido

    nombre = input('(-1) para cancelar la operación | Introduzca el nombre del equipo: ')

    if nombre == '-1':

        return None

    # Comprobramos que el nombre introducido forma parte o no
    # de equipamiento anteriormente definido

    for equipo in equipos:

        if isinstance(equipo, EquipoTermico) and equipo.nombre.lower() == nombre.lower():

            print('Equipo anteriormente definido. Extrayendo copia...')

            return copy.deepcopy(equipo)
    # Solicita el rango de temperaturas (mínima y máxima)
    rango = pedir_rango_temperatura()

    if rango is None:
        return None

    temp_max, temp_min = rango

    return EquipoTermico(nombre.lower(), temp_max, temp_min)


def pedir_rango_temperatura() -> Optional[Tuple[float, float]]:
    # Bucle de control para asegurar que ambas temperaturas formen un rango lógico y válido
    while True:

        temp_min = pedir_temperatura('Introduzca cualquier carácter para cancelar la operación | Introduzca la temperatura mínima (°C): ')

        if temp_min is None:

            return None
        

        temp_max = pedir_temperatura('Introduzca cualquier carácter para cancelar la operación | Introduzca la temperatura máxima (°C): ')

        if temp_max is None:

            return None
        
        try:
            # Invoca la validación del rango, si falla el flujo vuelve a empezar
            verificar_rango_temperatura(temp_max, temp_min)

            return temp_max, temp_min

        except ValueError:

            print('Introduzca temperaturas mínimas y máximas válidas.')



# Como -1 puede ser una temperatura válida, hace falta una función de pedir float diferente a la
# establecida en funciones.py

def pedir_temperatura(frase: str) -> Optional[float]:

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
            # Captura errores de entrada que no sean ni números válidos ni texto alfabético
            print('Introduzca una temperatura válida.')