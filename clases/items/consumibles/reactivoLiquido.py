from ..consumible import Consumible
from ..lote import Lote

from funciones import *

class ReactivoLiquido(Consumible):

    def __init__(self, nombre, lote, volumen: float):

        super().__init__(nombre, lote)
        self.volumen = volumen


    def __str__(self):
        return super().__str__() + f" | Vol: {self.volumen} ml"
    

    
    def __eq__(self, other):

        if isinstance(other, ReactivoLiquido):

            return self.nombre.lower() == other.nombre.lower() and self.volumen == other.volumen \
                and self.lote == other.lote

        return False
    
    

def importar_reactivo_liquido(consumibles: list, nombres: list, lote: Lote):

    # Esta función trabaja mediante referencia de lista, así que no hara falta return



    nombre_introducido = pedir_cadena_no_vacia('(0) para cancelar la importación | Introduzca el nombre del reactivo: ')

    if nombre_introducido is None:

        return
    


    volumen_introducido = pedir_unidades_float('(0) para cancelar la importación | Introduzca el volumen del reactivo (ml): ')

    if volumen_introducido is None:

        return
    


    unidades = pedir_unidades('(0) para cancelar la importación | Introduzca las unidades del reactivo: ')

    if unidades is None:

        return
    

    nombre_introducido = nombre_introducido.lower()
    repetido = False


    # Evitar repeticiones de nombres en diferentes tipos de clase
    if not nombre_introducido in nombres:


        # Si el consumible ha sido introducido anteriormente, se añaden las unidades
        for indice, reactivo_uds in enumerate(consumibles):

            # Se trata de una tupla, así que extraigo la instancia de consumible
            reactivo = reactivo_uds[0]

            if reactivo == ReactivoLiquido(nombre_introducido, lote, volumen_introducido):

                unidades_anteriores = reactivo_uds[1]

                consumibles[indice] = (reactivo, unidades + unidades_anteriores)

                repetido = True


        # Si no ha sido introducido anteriormente, se añade a la lista
        if not repetido:

            consumibles.append((ReactivoLiquido(nombre_introducido, lote, volumen_introducido), unidades))
            nombres.append(nombre_introducido)


    else:
        print('Se ve que un consumible con el mismo nombre ha sido introducido anteriormente. Cancelando importación...')