from abc import ABC, abstractmethod

from funciones import *

class Item(ABC):

    def __init__(self, nombre):

        self.nombre = nombre

    def __str__(self):
        return f"Item: {self.nombre}"
    
    def __eq__(self, other):

        if isinstance(other, Item):

            return self.nombre.lower() == other.nombre.lower()
        
        return False