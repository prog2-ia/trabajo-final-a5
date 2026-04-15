# El almacen de nuestro laboratorio podrá tener varios
# invetarios, cada uno con un nombre y una lista de items
from funciones import *

class Inventario():


    def __init__(self, nombre):
        self.nombre = nombre
        self.items = []