from abc import ABC, abstractmethod
from typing import Any

from funciones import *

class Item(ABC): # Hereda de ABC para marcar que es una clase abstracta base
    def __init__(self, nombre: str):
        # Todos los elementos del inventario (equipos o consumibles) tendrán, como mínimo, un nombre
        self.nombre: str = nombre

    def __str__(self) -> str:
        return f"Item: {self.nombre}"
    
    def __eq__(self, other: Any) -> bool:
        # Define la igualdad base para todo el sistema de herencia:
        # Dos ítems son iguales si pertenecen a la familia 'Item' y sus nombres coinciden (sin importar Mayús/Minús)
        if isinstance(other, Item):

            return self.nombre.lower() == other.nombre.lower()
        
        return False