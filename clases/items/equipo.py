from ..item import Item
from ..almacen import Inventario

from funciones import *

class Equipo(Item):

    dicc_estados = {0: "Operativo", 1: "Defectuoso", 2: "En uso"}   # Pasamos de número a texto descriptivo

    def __init__(self, nombre: str, estado: int):

        super().__init__(nombre)

        # El estado del equipo podra variar:
        # 0: En buen estado
        # 1: En mal estado, deberá ser tirado
        # 2: Siendo usado

        self.estado = estado

    def __str__(self):

        txt_estado = type(self).dicc_estados.get(self.estado, "Desconocido") # Evitar errores

        return super().__str__() + f" | Estado: {txt_estado}"
    
