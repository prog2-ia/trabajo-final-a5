from datetime import datetime

from funciones import *


# Trateremos la clase Registro como una sesión
class Registro():


    def __init__(self, cod, items):


        self.inicio = datetime.now()
        self.abierta = True


        self.items = items # Paquete con los objetos usados durante la sesión
        self.cod = cod # Código de la sesión, para identificarla en el registro


    def cerrar_sesion(self):

        # Hay que programarla de tal manera que los objetos de items
        # se devuelvan al inventario, y que se guarde el registro de la sesión

        self.fin = datetime.now()
        self.abierta = False


########################################################################
# A partir de aquí estarán las funciones de escritura en auditoria.txt #
########################################################################

#####################################
#       Funciones de almacen        #
#####################################

def escribir_creado_almacen(codigo):

    # datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Lo pasa al formato de fecha necesitado

    with open('logs/auditoria.txt', 'a') as archivo:

        archivo.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] - Creado nuevo almacen con codigo [{codigo}]\n')


def escribir_eliminado_almacen(inventario):

    with open('logs/auditoria.txt', 'a') as archivo:

        mensaje_inicial = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] - Almacén eliminado:\n'

        archivo.write(f'{mensaje_inicial}{str(inventario)}\n')


###################################
#       Funciones de equipo       #
###################################

def escribir_importar_equipo(equipo_cantidad_inventario: tuple):

    equipo   = equipo_cantidad_inventario[0][0] # Otra tupla de (equipo, cantidad)
    cantidad = equipo_cantidad_inventario[0][1]
    codigo   = equipo_cantidad_inventario[1]

    with open('logs/auditoria.txt', 'a') as archivo:

        mensaje_inicial = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] - Equipo ({cantidad} uds.) añadido al inventario [{codigo}]:\n'

        archivo.write(f'{mensaje_inicial}{str(equipo)}\n')


def escribir_mover_equipo(equipo_cantidad: tuple, codigo_origen: str, codigo_destino: str):

    equipo   = equipo_cantidad[0] # El equipo es el primer elemento de la tupla
    cantidad = equipo_cantidad[1] # La cantidad es el segundo elemento de la tupla

    with open('logs/auditoria.txt', 'a') as archivo:

        mensaje = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] - {str(equipo)} ({cantidad} uds.) movido del inventario [{codigo_origen}] al inventario [{codigo_destino}]\n'

        archivo.write(mensaje)



###################################
#       Funciones de lote         #
###################################


def escribir_nuevo_lote_definido(consumibles_inventario: tuple):

    consumibles = consumibles_inventario[0]
    inventario = consumibles_inventario[1]


    mensaje_cuerpo = ''
    unidades = 0
    for consumible in consumibles:

        mensaje_cuerpo += f'\n\t- {str(consumible[0])} ({consumible[1]} uds.)'
        unidades += consumible[1]

    

    mensaje_inicial = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] - Lote ({unidades} uds.) añadido a {inventario.codigo} .\n'


    with open('logs/auditoria.txt', 'a') as archivo:

        archivo.write(mensaje_inicial + mensaje_cuerpo)
    
    


