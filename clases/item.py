from abc import ABC, abstractmethod
from .almacen import Inventario

from funciones import *

class Item(ABC):

    def __init__(self, nombre):

        self.nombre = nombre

    def __str__(self):
        return f"Item: {self.nombre}"