from datetime import date

from funciones import *

class Lote():


    def __init__(self, id_lote: str, fecha_vencimiento: date, consumibles: list):

        # El id es constante, así que solo habrá getter
        self.__id_lote = id_lote

        # Las fechas son constante, así que solo habrá getter
        self.__fecha_vencimiento = fecha_vencimiento

        # Lista que contendrá los consumibles de un lote
        self.consumibles = consumibles



    # Como no se puede modificar el id ni la fecha, no habrá setter, solo getter
    
    @property   # Getter del id del lote
    def id_lote(self):
        return self.__id_lote
        

    @property   # Getter de la fecha de vencimiento del lote
    def fecha_vencimiento(self):
        return self.__fecha_vencimiento
        

    def esta_caducado(self):
        return date.today() > self.fecha_vencimiento
    
    def __eq__(self, other):

        if isinstance(other, Lote):

            return self.id_lote == other.id_lote
        
        return False
    
# Los IDs de los lotes tendrán forman 00-ABC
def comprobar_id_lote(id:str) -> bool:

    if len(id) != 6:

        return False
    
    return id[0:2].isdigit() and id[2] == '-' and id[3:6].isalpha()
    


# El usuario define un lote nuevo
def definir_lote(lotes: list):

    # Pasamos la lista de los lotes anteriormente definidos
    # Hara falta para ver que no hayan IDs repetidos

    while True:

        introducir_id = input('(0) para cancelar la operación | Introduzca el ID (00-ABC) del nuevo lote: ').upper()

        if introducir_id == '0':

            return None
        
        if comprobar_id_lote(introducir_id):


            # Comprobamos que no exista tal id en lotes anteriormente definidos
            for lote in lotes:


                if lote.id_lote == introducir_id:

                    print('Operación cancelada. Ya existe un lote con ese ID.')



        
        print('Introduzca un ID válido o (0) para cancelar la operación.')