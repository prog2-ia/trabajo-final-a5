class ReactivoSolido(Consumible):
    def __init__(self, nombre, fecha_vencimiento, stock, masa):
        super().__init__(nombre, fecha_vencimiento, stock)
        self.masa = masa
    def __str__(self):
        return f'Sólido: {self.nombre} | Stock: {self.stock} | Masa: {self.masa} | Vencimiento: {self.fecha_vencimiento}'