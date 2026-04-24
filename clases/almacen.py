import copy

from funciones import *

from .items.consumible import Consumible
from .items.equipo import Equipo

from .registro import Registro


# El almacen de nuestro laboratorio podrá tener varios
# invetarios, cada uno con un nombre y una lista de items

class Inventario():

    def __init__(self, codigo):
        self.__codigo = codigo
        self.items = []

        # Los items se guardaran en una tupla, el objeto item y la cantidad



    def __str__(self):

        frase_inicial = f'\n[{self.codigo}] con {len(self.items)} items\n\n'

        frase_items = ''

        for item in self.items:

            frase_items += f'\t- {str(item[0])}\n\t - Uds. disponibles: {item[1]}\n\n'

        return frase_inicial + frase_items

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

        return items_eliminados
    
    
    def anadir_item_al_inventario(self, item_cantidad):

        for indice, item in enumerate(self.items):

            # Comprueba si ya existía esa instancia para solo añadir
            # la cantidad
            if item[0] == item_cantidad[0]:

                self.items[indice][1] += item_cantidad[1]

                

# Pasamos una lista de inventarios
def mostrar_almacenes(inventarios):

    if len(inventarios) == 0:

        print('No hay almacenes disponibles.')
    
    else:

        print('Almacenes disponibles:')

        for inventario in inventarios:

            print(f'\n[{inventario.codigo}] con {len(inventario.items)} items\n\n')



def crear_almacen(inventarios):

    print('El código de un almacen debe ser 2 letras mayúsculas seguidas de 3 dígitos. Introduce 0 para cancelar la operación.')

    # El while True crear un bucle infinito que solo romperá un return
    while True:

        codigo_input = input('Introduce el código del nuevo almacén: ')


        try:

            codigo = verificar_codigo_almacen(codigo_input)

            if codigo == '-1':

                print('Operación cancelada.')
                return None


            if codigo in [inventario.codigo for inventario in inventarios]:

                print('Ya existe un almacén con ese código. Operación cancelada.')
                return None
            

            print(f'Creando nuevo almacén con código [{codigo}]... ')
            return Inventario(codigo)
        

        except ValueError as e:

            print(f'\n{e}\n')
            # Imprime el mensaje hecho en la función verificar_codigo_almacen y vuelve a pedir el código



# El código de un almacen será 2 letras mayúsculas seguidas de 3 dígitos
# Devolvemos -1 cuando el usuario quiera cancelar la operación
def verificar_codigo_almacen(codigo):

    match codigo:

        case '0':

            return '-1'
        
        case _:

            if len(codigo) == 5:

                if codigo[:2].isalpha() and codigo[:2].isupper() and codigo[2:].isdigit():

                    return codigo
                
            raise ValueError('Código no válido. El código debe ser 2 letras mayúsculas seguidas de 3 dígitos. Inténtalo de nuevo o introduce 0 para cancelar.')





def acceso_almacen(inventarios):

    while True:

        accedido = False

        # Menu de lo para acceder a un almacen concreto y ver su contenido
        print(f'\n\t[Código] - \tAcceder a un almacen\n'
            f'\t[0] - \tVolver atras\n'
        )

        # Tiene que tomar un código de almacen o 0 para volver atrás
        instruccion = input('\nAcceder a: ')

        for inventario in inventarios:

            if instruccion == inventario.codigo:

                print(inventario)
                accedido = True


        if instruccion == '0':

            print('Volviendo atrás...')
            return '0'
        
        
        if not accedido:

            print('Código no encontrado, vuelva a intentarlo.')





# Tengo que comentar esta función
def eliminar_almacen(inventarios):

    mostrar_almacenes(inventarios)

    while True:

        codigo_input = input('Introduce el código del almacén que quieres eliminar (0 para cancelar): ')

        if codigo_input == '0':

            print('Operación cancelada.')
            return '0'
        
        for inventario in inventarios:

            if codigo_input == inventario.codigo:

                confirmacion = input(f'¿Estás seguro de que quieres eliminar el almacén [{inventario.codigo}] y todos sus items? Esta acción no se puede deshacer. (s/n): ')

                if confirmacion.lower() == 's':

                    inventario_eliminado = copy.deepcopy(inventario) # Para mostrarlo en la auditoría

                    inventarios.remove(inventario)
                    print(f'Almacén [{inventario.codigo}] eliminado.')


                    return inventario_eliminado
                
                
                else:

                    print('Operación cancelada.')
                    return '0'
        
        print('Código no encontrado, vuelva a intentarlo.')




def anadir_item(item_cantidad: tuple, inventarios: list):

    mostrar_almacenes()


    print(f'\n\t[Código] - \tAñadir al almacen...\n'
            f'\t[0] - \tCancelar operación\n'
        )


    while True:

        # Tiene que tomar un código de almacen o 0 para volver atrás
        codigo_input = input('\nAñadir a: ')


        for inventario in inventarios:

            if inventario.codigo == codigo_input:

                inventario.anadir_item_al_inventario(item_cantidad)

                return (item_cantidad, inventario.codigo) 
                # Hacemos un return para triggear el mensaje de auditoría y para la función


        if codigo_input == '0':

            print('Cancelando operación...')
            return None
        
        else:

            print('Código no válido. Vuelva a intentarlo.')
    