from item import Consumible

class ReactivoLiquido(Consumible):

    def __init__(self, nombre, fecha_vencimiento, stock, volumen):
        super().__init__(nombre, fecha_vencimiento, stock)
        self.volumen = volumen

    def __str__(self):
        return f"Líquido: {self.nombre} | Stock: {self.stock} | Vol: {self.volumen}ml | Vencimiento: {self.fecha_vencimiento}"