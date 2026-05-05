from datetime import date

from .consumible import importar_consumible_generico
from .consumibles.reactivoSolido import importar_reactivo_solido
from .consumibles.reactivoLiquido import importar_reactivo_liquido

from funciones import *

class Lote():


    def __init__(self, id_lote: str, fecha_vencimiento: date):

        # El id es constante, así que solo habrá getter
        self.__id_lote = id_lote

        # Las fechas son constante, así que solo habrá getter
        self.__fecha_vencimiento = fecha_vencimiento




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
def definir_lote(lotes: dict):

    id_comprobado = False

    # Pasamos la lista de los lotes anteriormente definidos
    # Hara falta para ver que no hayan IDs repetidos

    while not id_comprobado:   # Este bucle se parara con un return o si el id introducido es válido


        introducir_id = input('(0) para cancelar la operación | Introduzca el ID (00-ABC) del nuevo lote: ').upper()

        if introducir_id == '0':

            return None
        

        
        if comprobar_id_lote(introducir_id):


            # Comprobamos que no exista tal id en lotes anteriormente definidos
            for lote in lotes.keys():


                if lote == introducir_id:

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
        
        
        # Comprobar que sea válida.
        if fecha_caducidad < date.today():

            print('Fecha no válida. No puedes importar lotes ya caducados.')

        else:

            return Lote(introducir_id, fecha_caducidad)
        

# Ahora hay que añadir consumibles al lote definido
def definir_lote_nuevo(lote: Lote):


    instruccion = ''

    consumibles = [] # Esta lista se desempaquetara a la hora de añadirla
                     # a un inventario

    nombres = [] # Para verificar no repetidos


    while not instruccion in ['4', '0']:

        instruccion = menu_consumibles()

        match instruccion:

            case '1': # Consumible genérico
                
                # Como las funciones trabaja mediante referencia de lista, no tiene return
                importar_consumible_generico(consumibles, nombres, lote)



            case '2': # Reactivo líquido

                importar_reactivo_liquido(consumibles, nombres, lote)



            case '3': # Reactivo solido

                importar_reactivo_solido(consumibles, nombres, lote)



            case '4':

                return consumibles


            case '0':

                return None


# Menu para que el usuario seleccione que consumible quiere añadir al lote
def menu_consumibles():

    print('\n\t[1] - Consumible genérico')
    print('\t[2] - Reactivo líquido')
    print('\t[3] - Reactivo solido')
    print('\t[4] - Finalizar lote')
    print('\t[0] - Cancelar lote')

    instruccion = input('Instrucción: ')

    if not instruccion in ['1', '2', '3', '4', '0']:

        return menu_consumibles()
    
    return instruccion