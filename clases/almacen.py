# El almacen de nuestro laboratorio podrá tener varios
# invetarios, cada uno con un nombre y una lista de items
from funciones import *

from .items.consumible import Consumible
from .items.equipo import Equipo


class Inventario():

    def __init__(self, codigo):
        self.__codigo = codigo
        self.items = []

        # Los items se guardaran en una tupla, el objeto item y la cantidad

    @property
    def codigo(self):
        return self.__codigo

    def quitar_vacios(self):

        # Elimina los items con cantidad 0 del inventario

        for item in self.items:

            if item[1] == 0:

                self.items.remove(item)


    def limpieza_inventario(self):

        # Elimina items caducados o en mal estado
        items_eliminados = [] # Para mostrarlo en la auditoría

        for item in self.items:

            if isinstance(item[0], Consumible):

                if item[0].__lote.esta_caducado():

                    items_eliminados.append(item[0])
                    self.items.remove(item)


            elif isinstance(item[0], Equipo):

                if item[0].estado == False: # Defectuoso

                    items_eliminados.append(item[0])
                    self.items.remove(item)


    def __str__(self):

        frase_inicial = f'\nInventario [{self.codigo}] con {len(self.items)} items\n\n'

        frase_items = ''

        for item in self.items:

            frase_items += f'\t- {str(item[0])}\n\t - Uds. disponibles: {item[1]}\n\n'

        return frase_inicial + frase_items


# Pasamos una lista de inventarios
def mostrar_almacenes(inventarios):

    print(inventario for inventario in inventarios)


# Se le pasa la lista de inventarios ya creados para comprobar que no hayan repetidos
def crear_almacen(inventarios):

    codigo_valido = False

    while not codigo_valido:

        codigo = input('Introduce el código del nuevo almacén: ')

        codigo_valido = verificar_codigo_almacen(codigo)    # Válidamos el código introducido por el usuario

        if codigo_valido == '-1':

            print('Operación cancelada.')
            return None
    
    
        if codigo in [inventario.codigo for inventario in inventarios]:

            print('Ya existe un almacén con ese código. Operación cancelada.')
            return None
        

        if not codigo_valido:

            print('Código no válido. El código debe ser 2 letras mayúsculas seguidas de 3 dígitos. Inténtalo de nuevo o introduce 0 para cancelar.')
    

    print(f'Creando nuevo almacén con código [{codigo}]... ')
    return Inventario(codigo)



# El código de un almacen será 2 letras mayúsculas seguidas de 3 dígitos
def verificar_codigo_almacen(codigo):

    if codigo == '0': # Para cancelar cualquier operación...

        return '-1'
    
    if len(codigo) != 5:

        return False
    
    if not codigo[:2].isalpha():

        return False
    
    if not codigo[:2].isupper():

        return False
    
    if not codigo[2:].isdigit():

        return False
    
    return True