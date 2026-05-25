import copy
from datetime import datetime, date
from typing import Optional, Dict, Any, List

# Para que el archivo main() no sea gigantesco,
# escribimos la mayoría de funciones básicas aquí

######################################################################
# Funciones para guardar y cargar el laboratorio                     #
######################################################################

import pickle
import os

def crear_auditoria():

    if not os.path.isdir('logs'):

        os.mkdir('logs')

    if not os.path.exists('logs/auditoria.txt'):

        with open('logs/auditoria.txt', 'x', encoding='utf-8') as fichero:

            fichero.write('Comienzo del registro del laboratorio.\n')
            fichero.close()


def cargar_laboratorio() -> Dict[str, Any]:
    # Intenta abrir el archivo binario pickle para restaurar el estado del sistema
    try:

        with open('datos/laboratorio.pkl', 'rb') as archivo:
            # Cargamos el diccionario maestro que contiene todo
            return pickle.load(archivo)
        
    except (FileNotFoundError, EOFError):
        # Si no hay archivo, creamos la estructura base vacía

        if not os.path.isdir('datos'):

            os.mkdir('datos')

        return {
            "lista_inventarios": [],
            "lista_sesiones": [],
            "equipos": [],
            "lotes": {}
        }


def guardar_laboratorio(datos_a_guardar):
    # Serializa y vuelca el diccionario maestro de laboratorio en el archivo binario
    with open('datos/laboratorio.pkl', 'wb') as archivo:

        pickle.dump(datos_a_guardar, archivo)

# Está función modificara las listas de los archivos pickle

def anadir_equipo_definido(equipo, equipos: list):
    # NOTA: Al modificar la lista por referencia directa, los cambios persisten fuera de la función.
    # Registra un clon del equipo en el catálogo histórico global si no fue guardado previamente.
    if not equipo in equipos:

        equipos.append(copy.deepcopy(equipo))

    # Como hace referencia a una lista lo que se edita, no hace falta hacer return


######################################################################

# Se usa para navegar entre los menus
def pedir_num(frase: str) -> Optional[str]:

    print(frase, end='')

    numero = input().strip()

    # Comprueba que sea un número
    if numero.isdigit():

        return numero
    
        # Aunque se pida un número, se devuelve un str para evitar errores
    
    return None
    
    # Si el usuario no introduce un número, devolvemos None
    # El 0 está reservado para salir de capas de menu



def pedir_int(frase: str) -> Optional[int]:
    # Obliga al usuario a meter un entero positivo
    while True:

        print(frase, end='')
        numero = input()

        if numero == '-1': # Cancelación

            return None
        
        try:
            # Aseguramos que no sea un float camuflado (4.5) y que sea mayor que 0
            if int(numero) == float(numero) and int(numero) > 0:

                return int(numero)
            
            raise ValueError


        except ValueError:

            print('Introduzca un número entero positivo.\n')


def pedir_int_entre_valores(frase, valor_min, valor_max):
    # Entero validado positivamente
    numero = pedir_int(frase)

    if numero is None:

        return None
    # Comprobación de límites operacionales
    if valor_min > numero or numero > valor_max:

        print(f'Introduzca un número válido [{valor_min}, {valor_max}]\n')
        return pedir_int_entre_valores(frase, valor_min, valor_max) # Reintento mediante recursividad
    
    return numero
    


def pedir_float(frase):
    # Captura valores decimales (negativos también)
    while True:

        print(frase, end='')

        numero = input()

        if numero == '-1':

            return None
        
        try:

            return float(numero)
        
        except ValueError:

            print('Error. Introduzca un valor numérico válido.\n')



def pedir_fecha(frase: str) -> Optional[date]:

    while True:

        print(frase, end='')
        fecha_str = input()


        if fecha_str == '0':
            return None

        try:
            # formato estricto DD/MM/AAAA

            fecha_parseada = datetime.strptime(fecha_str, "%d/%m/%Y")
            
            # 3. Como strptime devuelve fecha Y hora, usamos .date() para quedarnos solo con el día
            return fecha_parseada.date()


        except ValueError:
            # Si el usuario escribe "hola", "32/13/2024" o usa guiones en lugar de barras, salta aquí
            print('Formato de fecha incorrecto o fecha no válida. Use el formato DD/MM/AAAA.\n')



def pedir_cadena_no_vacia(frase):

    while True:

        print(frase, end='')
        cadena = input().strip() # Quita espacios delante y detrás

        if cadena == '0':

            return None
        
        if cadena: # Si la cadena evalúa a True, no está vacía
        
            return cadena
        
        print('Error: El texto no puede estar vacío o contener solo espacios.')
        
##################################################################################
# En estas dos funciones se pediran números mayores que 0                        #
##################################################################################

def pedir_unidades(frase):
    # Validación de cantidades enteras para inventario
    while True:

        print(frase, end='')
        unidades = input()


        if unidades == '0':

            return None

        try:

            if int(unidades) == float(unidades) and int(unidades) > 0:

                return int(unidades)
            
            raise ValueError


        except ValueError:

            print('Introduzca un valor numérico válido.\n')


def pedir_unidades_float(frase):

    # Útil para ml o gramos
    while True:

        print(frase, end='')
        unidades = input()

        if unidades == '0':

            return None

        try:

            if float(unidades) > 0:

                return float(unidades)
            
            raise ValueError


        except ValueError:

            print('Introduzca un valor numérico válido.\n')


##################################################################################