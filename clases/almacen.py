# El almacen de nuestro laboratorio podrá tener varios
# invetarios, cada uno con un nombre y una lista de items
from funciones import *

class Inventario():

    inventarios = []   # Lista de inventarios del almacen

    def __init__(self, nombre):
        self.nombre = nombre
        self.items = []

        Inventario.inventarios.append(self)
        # Tener una lista de inventarios nos ayudara a gestionar los inventarios
        # del almacen de manera más comoda