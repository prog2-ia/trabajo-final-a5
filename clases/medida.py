from equipo import Equipo

class EquipoMedida(Equipo):
    def __init__(self, nombre, inventario, cantidad, estado, error_medida: float):
        super().__init__(nombre, inventario, cantidad, estado)
        self.error_medida = error_medida

    def __str__(self):
        return super().__str__() + f" | Error: ±{self.error_medida}"