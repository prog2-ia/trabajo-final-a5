from item import Item
from almacen import Inventario

class Equipo(Item):

    def __init__(self, nombre: str, inventario: Inventario, cantidad: int, estado: int):

        super().__init__(nombre, inventario, cantidad)

        # El estado del equipo podra variar:
        # 0: En buen estado
        # 1: En mal estado, deberá ser tirado
        # 2: Siendo usado

        self.estado = estado

    def __str__(self):

        pass
    
