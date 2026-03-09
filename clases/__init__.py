# Importamos las clases de los archivos internos

from item import Item
from consumible import Consumible
from equipo import Equipo

# Volvemos los paquetes públicos para que sean importados en main.py
__all__ = ['Item', 'Consumible', 'Equipo']