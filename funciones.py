import copy
from datetime import datetime

# Para que el archivo main() no sea gigantesco,
# escribimos la mayoría de funciones básicas aquí

######################################################################
# Funciones para guardar y cargar el laboratorio                     #
######################################################################

import pickle

def cargar_laboratorio():

    try:

        with open('datos/laboratorio.pkl', 'rb') as archivo:
            # Cargamos el diccionario maestro que contiene todo
            return pickle.load(archivo)
        
    except (FileNotFoundError, EOFError):
        # Si no hay archivo, creamos la estructura base vacía
        return {
            "lista_inventarios": [],
            "lista_sesiones": [],
            "equipos": [],
            "lotes": {}
        }

def guardar_laboratorio(datos_a_guardar):

    with open('datos/laboratorio.pkl', 'wb') as archivo:

        pickle.dump(datos_a_guardar, archivo)

# Está función modificara las listas de los archivos pickle

def anadir_equipo_definido(equipo, equipos: list):

    if not equipo in equipos:

        equipos.append(copy.deepcopy(equipo))

    # Como hace referencia a una lista lo que se edita, no hace falta hacer return


######################################################################

# Se usa para navegar entre los menus
def pedir_num(frase):

    print(frase, end='')

    numero = input()

    # Comprueba que sea un número
    if numero.isdigit():

        return numero
    
        # Aunque se pida un número, se devuelve un str para evitar errores
    
    return None
    
    # Si el usuario no introduce un número, devolvemos None
    # El 0 está reservado para salir de capas de menu



def pedir_int(frase):

    while True:

        print(frase, end='')
        numero = input()

        if numero == '-1':

            return None
        
        try:

            if int(numero) == float(numero) and int(numero) > 0:

                return int(numero)
            
            raise ValueError


        except ValueError:

            print('Introduzca un número entero positivo.\n')


def pedir_int_entre_valores(frase, valor_min, valor_max):

    numero = pedir_int(frase)

    if numero is None:

        return None
    
    if valor_min > numero or numero > valor_max:

        print(f'Introduzca un número válido [{valor_min}, {valor_max}]\n')
        return pedir_int_entre_valores(frase, valor_min, valor_max)
    
    return numero
    


def pedir_float(frase):

    while True:

        print(frase, end='')

        numero = input()

        if numero == '-1':

            return None
        
        try:

            return float(numero)
        
        except ValueError:

            print('Error. Introduzca un valor numérico válido.\n')



def pedir_fecha(frase):

    while True:

        print(frase, end='')
        fecha_str = input()


        if fecha_str == '0':
            return None

        try:
            

            fecha_parseada = datetime.strptime(fecha_str, "%d/%m/%Y")
            
            # 3. Como strptime devuelve fecha Y hora, usamos .date() para quedarnos solo con el día
            return fecha_parseada.date()


        except ValueError:
            # Si el usuario escribe "hola", "32/13/2024" o usa guiones en lugar de barras, salta aquí
            print('Formato de fecha incorrecto o fecha no válida. Use el formato DD/MM/AAAA.\n')



def pedir_cadena_no_vacia(frase):

    while True:

        print(frase, end='')
        cadena = input()

        if cadena == '0':

            return None
        
        if cadena.strip() and cadena.strip() != '0':
        
            return cadena
        
##################################################################################
# En estas dos funciones se pediran números mayores que 0                        #
##################################################################################

def pedir_unidades(frase):

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