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