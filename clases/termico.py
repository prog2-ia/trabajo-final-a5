from equipo import Equipo

class EquipoTermico(Equipo):
    def __init__(self, nombre, inventario, cantidad, estado, temp_max: float, temp_min: float):
        super().__init__(nombre, inventario, cantidad, estado)
        self.temp_max = temp_max
        self.temp_min = temp_min

    def __str__(self):
        return super().__str__() + f" | Rango: {self.temp_min}º a {self.temp_max}º"