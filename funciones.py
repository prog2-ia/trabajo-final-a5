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
            "lotes": []
        }

def guardar_laboratorio(datos_a_guardar):

    with open('datos/laboratorio.pkl', 'wb') as archivo:

        pickle.dump(datos_a_guardar, archivo)


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
    
    # Si el usuario no introduce un número, devolvemos -1
    # El 0 está reservado para salir de capas de menu



def pedir_int(frase):

    while True:

        print(frase, end='')
        numero = input()

        if numero == '-1':

            return None
        
        try:

            if int(numero) == float(numero):

                return int(numero)
            
            else:

                print('Introduzca un número entero positivo.')

        except ValueError:

            print('Introduzca un número entero positivo.')


def pedir_int_entre_valores(frase, valor_min, valor_max):

    numero = pedir_int(frase)

    if numero is None:

        return None
    
    if valor_min > numero or numero > valor_max:

        print(f'Introduzca un número válido [{valor_min}, {valor_max}]')
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

            print('Error. Introduzca un valor numérico válido.')
