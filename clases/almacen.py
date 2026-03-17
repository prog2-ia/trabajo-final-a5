# El almacen de nuestro laboratorio podrá tener varios
# invetarios, cada uno con un nombre y una lista de items

class Inventario():

    def __init__(self, nombre):
        self.nombre = nombre
        self.items = []