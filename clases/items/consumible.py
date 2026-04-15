from ..item import Item
from ..almacen import Inventario
from .lote import Lote

class Consumible(Item):

    def __init__(self, nombre: str, inventario: Inventario, cantidad: int, lote: Lote):

        super().__init__(nombre, inventario, cantidad)
        self.__lote = lote  # No se podra mofidicar
                            # El lote de un consumible representa su fecha de vencimiento
                            # Entonces no tendrá setter

    def __str__(self):
        id_lote = self.__lote.id_lote
        fecha = self.__lote.fecha_vencimiento
        # compruebo si el consumible está caducado con la función de lote
        estado_lote = "CADUCADO" if self.__lote.esta_caducado() else "En fecha"
        return f"{super().__str__()} | Lote: {id_lote} | Vence: {fecha} ({estado_lote})"