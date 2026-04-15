from datetime import date

class Lote():

    lotes = []  # Lista de lotes creados

    def __init__(self, id_lote: str, fecha_vencimiento: date):

        # El id es constante, así que solo habrá getter
        self.__id_lote = id_lote

        # Las fechas son constante, así que solo habrá getter
        self.__fecha_vencimiento = fecha_vencimiento
        Lote.lotes.append(self)


    @property   # Getter del id del lote
    def id_lote(self):
        return self.__id_lote
        

    @property   # Getter de la fecha de vencimiento del lote
    def fecha_vencimiento(self):
        return self.__fecha_vencimiento
        

    def esta_caducado(self):
        return date.today() > self.fecha_vencimiento