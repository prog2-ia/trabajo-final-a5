from ..item import Item
from .lote import Lote

from funciones import *

class Consumible(Item):

    def __init__(self, nombre: str, lote: Lote):

        super().__init__(nombre)
        self.__lote = lote  # No se podra mofidicar
                            # El lote de un consumible representa su fecha de vencimiento
                            # Entonces no tendrá setter


    def __str__(self):


        id_lote = self.__lote.id_lote
        fecha = self.__lote.fecha_vencimiento

        # Compruebo si el consumible está caducado con la función de lote

        if self.__lote.esta_caducado():
            estado_lote = "CADUCADO"
        else:
            estado_lote = "En fecha"

        return f"{super().__str__()} | Lote: {id_lote} | Vence: {fecha} ({estado_lote})"
    

    def __eq__(self, other):

        if isinstance(other, Consumible):

            return super().__eq__(other) and self.__lote == other.__lote


        return False
    


# Función usada en la definición de nuevo lote
def importar_consumible_generico(consumibles: list, lote: Lote):

    # Esta función trabaja mediante referencia de lista, así que no hara falta return



    nombre_introducido = pedir_cadena_no_vacia('(0) para cancelar la importación | Introduzca el nombre del consumible: ')

    if nombre_introducido is None:

        return


    unidades = pedir_int('(0) para cancelar la importación | Introduzca las unidades del consumible: ')


    if unidades is None:

        return



    nombre_introducido = nombre_introducido.lower()
    repetido = False


    # Si el consumible ha sido introducido anteriormente, se añaden las unidades
    for indice, consumible_uds in enumerate(consumibles):

        # Se trata de una tupla, así que extraigo la instancia de consumible
        consumible = consumible_uds[0]

        if consumible.nombre == nombre_introducido:

            unidades_anteriores = consumible_uds[1]

            consumibles[indice] = (consumible, unidades + unidades_anteriores)

            repetido = True


    # Si no ha sido introducido anteriormente, se añade a la lista
    if not repetido:

        consumibles.append((Consumible(nombre_introducido, lote), unidades))
