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


def pedir_num(frase):

    print(frase, end='')

    numero = input()

    # Comprueba que sea un número
    if numero.isdigit():

        return numero
    
        # Aunque se pida un número, se devuelve un str para evitar errores
    
    return '-1'
    
    # Si el usuario no introduce un número, devolvemos -1
    # El 0 está reservado para salir de capas de menu



def pedir_int(frase):

    print(frase, end='')
    numero = input()

    if numero == '-1':

        return '-1'
    
    if numero.isdigit():

        return int(numero)
    
    
    return pedir_int(frase)