from abc import ABC, abstractmethod
from .almacen import Inventario

from funciones import *

class Item(ABC):

    def __init__(self, nombre, inventario: Inventario, cantidad=1):

        self.nombre = nombre
        self.__inventario = inventario
        self.cantidad = cantidad

        inventario.items.append(self)   # Agrega el item al inventario

    def __str__(self):
        return f"Item: {self.nombre} (Cant: {self.cantidad})"

    @property   # Getter del inventario donde se guarda el item
    def inventario(self):
        return self.__inventario
    
    @inventario.setter   # Setter del inventario donde se guarda el item
    def inventario(self, nuevo_inventario):

        if isinstance(nuevo_inventario, Inventario):
            
            # Elimina el item del inventario actual antes de asignarlo al nuevo inventario
            if self.__inventario is not None:
                self.__inventario.items.remove(self)

            # El is 'not None' comprueba si el item ya tiene un inventario asignado

            self.__inventario = nuevo_inventario
            nuevo_inventario.items.append(self)   # Mueve el item al nuevo inventario