# El almacen de nuestro laboratorio podrá tener varios
# invetarios, cada uno con un nombre y una lista de items
from funciones import *

class Inventario():

    def __init__(self, codigo):
        self.codigo = codigo
        self.items = []

        # Los items se guardaran en una tupla, el objeto item y la cantidad

    def quitar_vacios(self):

        # Elimina los items con cantidad 0 del inventario

        for item in self.items:

            if item[1] == 0:

                self.items.remove(item)


    def __str__(self):

        frase_inicial = f'\nInventario [{self.codigo}] con {len(self.items)} items:\n\n'

        frase_items = ''

        for item in self.items:

            frase_items += f'\t- {str(item[0])}\n\t - Uds. disponibles: {item[1]}\n\n'

        return frase_inicial + frase_items


# Pasamos una lista de inventarios
def mostrar_almacenes(inventarios):

    print(inventario for inventario in inventarios)
