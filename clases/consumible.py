from item import Item
from almacen import Inventario
from lote import Lote

class Consumible(Item):

    def __init__(self, nombre: str, inventario: Inventario, cantidad: int, lote: Lote):

        super().__init__(nombre, inventario, cantidad)
        self.__lote = lote  # No se podra mofidicar
                            # El lote de un consumible representa su fecha de vencimiento
                            # Entonces no tendrá setter

    def __str__(self):

        pass