import datetime

from funciones import *


# Trateremos la clase Registro como una sesión
class Registro():


    def __init__(self, cod, items):


        self.inicio = datetime.datetime.now()
        self.abierta = True


        self.items = items # Paquete con los objetos usados durante la sesión
        self.cod = cod # Código de la sesión, para identificarla en el registro


    def cerrar_sesion(self):

        # Hay que programarla de tal manera que los objetos de items
        # se devuelvan al inventario, y que se guarde el registro de la sesión

        self.fin = datetime.datetime.now()
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

        archivo.write(f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] - Creado nuevo almacen con codigo [{codigo}]\n')


def escribir_eliminado_almacen(inventario):

    with open('logs/auditoria.txt', 'a') as archivo:

        mensaje_inicial = f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] - Almacén eliminado:\n'

        archivo.write(f'{mensaje_inicial}{str(inventario)}\n')