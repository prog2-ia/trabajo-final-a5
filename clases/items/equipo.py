from ..item import Item

from funciones import *

class Equipo(Item):

    dicc_estados = {True: "Buen estado", False: "Defectuoso"}

    def __init__(self, nombre: str, estado: bool):

        super().__init__(nombre)

        # True -> Buen estado | False -> Defectuoso

        self.estado = estado


    def __str__(self):

        txt_estado = type(self).dicc_estados.get(self.estado, "Desconocido") # Evitar errores

        return super().__str__() + f" | Estado: {txt_estado}"
    

    def __eq__(self, other):

        if isinstance(other, Equipo):

            return super().__eq__(other) and self.estado == other.estado
        
        return False
    
