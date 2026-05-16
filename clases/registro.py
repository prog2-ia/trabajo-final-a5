from datetime import datetime
from typing import List, Any

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


# Verificar que el código introducido sea válido
def verificar_codigo(cod: str):

    match cod:

        case '0':

            return None
        
        case _:

            if len(cod) == 5:

                if cod[:3].isalpha() and cod[:3].isupper() and cod[3:].isdigit():

                    return True

            raise ValueError('Código no válido. El código debe ser 3 letras mayúsculas y 2 números.')



# Se le pasa la lista con las sesiones abiertas
def crear_sesion(sesiones:list):


    while True:

        codigo_input = input('0 para cancelar | Introduzca el código de la nueva sesión: ')

        try:

            verificacion = verificar_codigo(codigo_input)

            if verificacion is None:

                return None
            
            '''
            if not codigo_input in sesiones:

                return Registro(codigo_input, [])
            
            else:

                print('Ya existe una sesión con ese código. Por favor use otro.')
            '''


            for sesion in sesiones:

                codigo = sesion.cod

                if codigo_input == codigo:

                    print('Ya existe una sesión con ese código.\n')
                    verificacion = False

            if verificacion:

                return codigo

            
        except ValueError as e:

            print(f'\n{e}\n')


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


def escribir_limpieza_inventarios(diccionario_limpieza: dict):

    mensaje_inicial = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] - Limpieza de almacenes\n\n'

    cuerpo_mensaje = ''

    for inventario_sucio in diccionario_limpieza:

        limpiado = diccionario_limpieza[inventario_sucio]

        # Comprueba que no este vacio, si esta vacio no se muestra
        if limpiado:

            cuerpo_mensaje += f'\t[{inventario_sucio}]\n\n'

            # Se añadían a la lista de limpiados los items con sus unidades
            for item in limpiado:

                cuerpo_mensaje += f'\t\t - {str(item[0])} | [{item[1]}] uds.\n'


    mensaje_final = mensaje_inicial + cuerpo_mensaje + '\n'


    with open('logs/auditoria.txt', 'a') as archivo:

        archivo.write(mensaje_inicial) 





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

    codigo = ''
    mensaje_cuerpo = ''
    unidades = 0
    for consumible in consumibles:

        if unidades == 0:

            codigo = consumible[0].lote

        mensaje_cuerpo += f'\n\t- {str(consumible[0])} ({consumible[1]} uds.)'
        unidades += consumible[1]


    mensaje_inicial = f'\n[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] - Lote ({codigo}) ({unidades} uds.) añadido a {inventario.codigo}.\n'


    with open('logs/auditoria.txt', 'a') as archivo:

        archivo.write(mensaje_inicial + mensaje_cuerpo)



    
    
###################################
#       Funciones de sesion       #
###################################


def escribir_sesion_empezada(sesion: Registro):

    items   = sesion.items
    codigo  = sesion.cod
    fecha_inicio = sesion.inicio

    cuerpo_mensaje = ''

    for item in items:

        cuerpo_mensaje += f'\t - {str(item[0])}\n\t\t({item[1]}) uds. \t| [{item[2].codigo}]'


    mensaje_inicial = f'\n[{fecha_inicio}] Sesión con código ({codigo}) comenzada\n'

    

    with open('logs/auditoria.txt', 'a') as archivo:

        archivo.write()

