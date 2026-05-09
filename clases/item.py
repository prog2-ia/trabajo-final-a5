from abc import ABC, abstractmethod
from typing import Any

from funciones import *

class Item(ABC):

    def __init__(self, nombre: str):

        self.nombre: str = nombre

    def __str__(self) -> str:
        return f"Item: {self.nombre}"
    
    def __eq__(self, other: Any) -> bool:

        if isinstance(other, Item):

            return self.nombre.lower() == other.nombre.lower()
        
        return False