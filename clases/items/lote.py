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
    


# El usuario define un lote nuevo, aunque se seleccione un lote
# anteriormente definido, habría que cambiar la fecha y el ID
def definir_lote(lotes: list):

    id_comprobado = False

    # Pasamos la lista de los lotes anteriormente definidos
    # Hara falta para ver que no hayan IDs repetidos

    while not id_comprobado:   # Este bucle se parara con un return o si el id introducido es válido


        introducir_id = input('(0) para cancelar la operación | Introduzca el ID (00-ABC) del nuevo lote: ').upper()

        if introducir_id == '0':

            return None
        

        
        if comprobar_id_lote(introducir_id):


            # Comprobamos que no exista tal id en lotes anteriormente definidos
            for lote in lotes:


                if lote.id_lote == introducir_id:

                    print('Ya existe un lote con ese ID.')
                    return None
                
            
            id_comprobado = True
            

        if not id_comprobado:

            print('Introduzca un ID válido o (0) para cancelar la operación.')


    # A partir de aquí se pide la fecha
    while True:

        fecha_caducidad = pedir_fecha('(0) para cancelar | Introduzca la fecha de caducidad (DD/MM/AAAA): ')

        if fecha_caducidad is None:

            return None
        
        if fecha_caducidad < date.today():

            print('Fecha no válida. No puedes importar lotes ya caducados.')

        else:

            return introducir_id, fecha_caducidad
        

# En esta función se añaden los consumibles
def definir_lote_nuevo(id, fecha_caducidad):

    instruccion = ''

    print('Introduzca (1) para terminar de añadir consumibles al lote o (0) para cancelar la operación.')

    while instruccion:

        pass