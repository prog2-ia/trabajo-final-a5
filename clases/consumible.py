from item import Item

class Consumible(Item):

    def __init__(self, nombre, fecha_vencimiento, stock=0):

        super().__init__(nombre, fecha_vencimiento, stock)