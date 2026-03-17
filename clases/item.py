from abc import ABC, abstractmethod
from almacen import Inventario

class Item(ABC):

    def __init__(self, nombre, inventario, stock=1):

        self.nombre = nombre
        self.__inventario = inventario
        self.__stock = stock

    @property   #getter del inventario donde se guarda el item
    def inventario(self):
        return self.__inventario
    
    @inventario.setter   #setter del inventario donde se guarda el item
    def inventario(self, nuevo_inventario):

        if isinstance(nuevo_inventario, Inventario):
        self.__inventario = nuevo_inventario
    
