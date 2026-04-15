from ..consumible import Consumible

class ReactivoLiquido(Consumible):
    def __init__(self, nombre, inventario, cantidad, lote, volumen: float):
        super().__init__(nombre, inventario, cantidad, lote)
        self.volumen = volumen

    def __str__(self):
        return super().__str__() + f" | Vol: {self.volumen}ml"